
import numpy as np

def access_font_data(font, unit_scale):
    Font= np.load(font)
    if unit_scale:
        return Font /255.
    return Font

class FontDataprovider(object):
    def __init__(self,font,start,end):
        self.start=start
        self.end = end
        self.data = np.copy(font[start: end])
        self.cursor = 0
        self.length = self.end - self.start

    def get_data(self):
        return self.data

    def next_batch(self,batch_size):
        if self.cursor >= self.length:
            self.cursor = 0
        batch_start = self.cursor
        batch_end = self.cursor + batch_size
        self.cursor += batch_size
        return self.data[batch_start: batch_end]


class FontDataManager(object):
    def __init__(self,src,target,total,split_point,unit_scale=True,shuffle=False):
        src_data=access_font_data(src,unit_scale)
        target_data= access_font_data(target,unit_scale)
        if shuffle:
            perm=np.arange(src_data.shape[0])
            np.random.shuffle(perm)
            src_data = src_data[perm]
            target_data = target_data[perm]
        self.train_source= FontDataprovider(src_data,0,split_point)
        self.validation_source=FontDataprovider(src_data,split_point,total)
        self.train_target= FontDataprovider(target_data,0,split_point)
        self.validation_target=FontDataprovider(target_data,split_point,total)

    def next_train_batch(self,batch_size):
        if self.train_source.cursor >= self.train_source.length:
            perm = np.arange(self.train_source.length)
            np.random.shuffle(perm)
            self.train_source.data = self.train_source.data[perm]
            self.train_target.data = self.train_target.data[perm]
        return self.train_source.next_batch(batch_size), self.train_target.next_batch(batch_size)

    def get_validation(self):
        return self.validation_source.get_data(),self.validation_target.get_data()
