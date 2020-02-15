from transloadit import client

tl = client.Transloadit('x',
                        'x')
assembly = tl.new_assembly()

assembly.add_step(':original', {
    'robot': '/upload/handle'
})

assembly.add_step('hevc_encoded', {
    'use': ':original',
    'robot': '/video/encode',
    'result': true,
    'ffmpeg_stack': 'v3.3.3',
    'preset': 'hevc',
    'width': 3840,
    'height': 1736
    "ffmpeg": {
        "crf": 30,
        "preset": "placebo",
        "vsync": 2
    }
})
assembly.add_step('exported', {
    'use': ['hevc_encoded', ':original'],
    'robot': '/file/compress',
    "result": true,
    "compression_level": -9
    "format": "zip"
})

assembly.add_file(open('./Ip.Man.4.mp4', 'rb'))
assembly_response = assembly.create(retries=5, wait=True)
print(assembly_response.data)
