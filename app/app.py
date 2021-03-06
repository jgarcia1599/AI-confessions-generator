from starlette.applications import Starlette
from starlette.responses import JSONResponse
import gpt_2_simple as gpt2
import tensorflow as tf
import uvicorn
import os
import gc
import re
app = Starlette(debug=False)

sess = gpt2.start_tf_sess(threads=1)
gpt2.load_gpt2(sess)

# Needed to avoid cross-domain issues
response_header = {
    'Access-Control-Allow-Origin': '*'
}

generate_count = 0


@app.route('/', methods=['GET', 'POST', 'HEAD'])
async def homepage(request):
    global generate_count
    global sess

    if request.method == 'GET':
        params = request.query_params
    elif request.method == 'POST':
        params = await request.json()
    elif request.method == 'HEAD':
        return JSONResponse({'text': ''},
                             headers=response_header)
    print('+++++++++++++++')
    print(params)
    text = gpt2.generate(sess,
                         length=100,
                         temperature=float(params.get('temperature', 0.7)),
                         prefix=params.get('prefix', '')[:500],
                         return_as_list=True
                         )[0]

    generate_count += 1
    if generate_count == 8:
        # Reload model to prevent Graph/Session from going OOM
        tf.reset_default_graph()
        sess.close()
        sess = gpt2.start_tf_sess(threads=1)
        gpt2.load_gpt2(sess)
        generate_count = 0

    gc.collect()
    text = re.split('\n', text)
    return JSONResponse({'text': text},
                         headers=response_header)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
