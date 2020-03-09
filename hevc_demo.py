from transloadit import client

tl = client.Transloadit('x','x')
assembly = tl.new_assembly()

assembly.add_step('hevc_encoded','/video/encode', {
    'use': ':original',
    'result': True,
    'ffmpeg_stack': 'v3.3.3',
    'preset': 'hevc',
    'width': 1920,
    'height': 1080,
    "ffmpeg": {
        "crf": 30,
        "preset": "placebo",
    }
})
assembly.add_step('exported','/file/compress', {
    'use': ['hevc_encoded', ':original'],
    "result": True,
    "compression_level": -9,
    "format": "zip"
})

assembly.add_file(open('./Super.mp4', 'rb'))
assembly_response = assembly.create(retries=5, wait=True)
print(assembly_response.data)