import networks
import torch
import numpy as np
import time
import os

def normalize(_tensor):
    return (_tensor - 0.5)/0.5

def unnormalize(_tensor):
    return (_tensor*0.5) + 0.5

class Artist:
    def __init__(self, model_dir):
        self.num_classes = 182

        self.network = getattr(networks, 'SegInNet')(4,3).cuda()
        print('Load model: ' + os.path.basename(model_dir))
        self.network.load_state_dict(torch.load(model_dir)['transformer'])
        self.network.eval()

    def stylize(self, img_np):

        img_tensor = torch.FloatTensor(img_np.transpose((2, 0, 1)).astype(np.float32) * (1.0 / 255.0)).unsqueeze(0)
        img_tensor = img_tensor.cuda()

        seg_tensor = torch.zeros_like(img_tensor)[:,0,:,:].unsqueeze(1)
        seg_tensor = seg_tensor.cuda()

        # normalize
        seg_tensor = normalize(seg_tensor)
        img_tensor = normalize(img_tensor)

        _ctime = time.time()
        tensor_out = self.network(img_tensor, seg_tensor)
        computation_time = time.time() - _ctime + 1e-8
        print('FPS: {}'.format(round(1/computation_time, 2)))

        tensor_out = unnormalize(tensor_out)

        img_tensor = img_tensor.cpu()
        seg_tensor = seg_tensor.cpu()
        tensor_out = tensor_out.cpu()

        img_out = tensor_out[0,:, :, :].detach().numpy().transpose(1, 2, 0) * 255.0

        return img_out.astype(np.uint8)

