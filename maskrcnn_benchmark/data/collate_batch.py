# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
from maskrcnn_benchmark.structures.image_list import to_image_list


class BatchCollator(object):
    """
    From a list of samples from the dataset,
    returns the batched images and targets.
    This should be passed to the DataLoader
    """

    def __init__(self, size_divisible=0):
        self.size_divisible = size_divisible

    def __call__(self, batch):
        transposed_batch = list(zip(*batch))
        images = to_image_list(transposed_batch[0], self.size_divisible)
        #images = to_image_list(transposed_batch[0])
        targets = transposed_batch[1]
        mask = to_image_list(transposed_batch[2], self.size_divisible)
        #mask = transposed_batch[2]
        img_ids = transposed_batch[3]
        return images, targets, mask,img_ids