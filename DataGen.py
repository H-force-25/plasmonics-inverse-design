import numpy as np
from scattnlay import scattnlay

'''
'''

class DataGen:
    def __init__(self, mats_indices, thicknesses, host='air'):
        self.mat_list = ('', 'ag', 'al', 'au', 'cu', 'gaas', 'inas', 'inp', 'mo', 'si', 'sio2')
        self.mats = self.gen_mat_list(mats_indices)
        self.radii = np.cumsum(thicknesses)
        self.host = host

    def get_mat_list(self):
        return self.mat_list
    
    def get_mat_index(self, mat):
        if mat in self.mat_list:
            return self.mat_list.index(mat)
        else:
            print('Invalid Material.')
            return None

    def gen_mat_list(self, mats_indices):
        # example mats_indices=(1,3,5) returns ['ag', 'al', 'tio2']
        mats = [self.mat_list[int(i)] for i in np.array(mats_indices, ndmin=1)]
        while '' in mats:
            mats.remove('')
        return mats
    
    def generate(self):
        # Dielectric properties
        df_diel = np.genfromtxt(f'./Refractive index interpolated/n_{self.host}.csv', delimiter=',', skip_header=1)
        m_diel = df_diel[:,1] + df_diel[:,2]*1j


        # Initializing wavelength and shapes of x and m
        wavelength = df_diel[:,0] * 1e-6

        x = np.zeros((wavelength.size, len(self.mats)), dtype=np.float32)
        m = np.zeros((wavelength.size, len(self.mats)), dtype=np.complex128)


        # Material properties
        for i, mat in enumerate(self.mats):
            df = np.genfromtxt(f'./Refractive index interpolated/n_{mat}.csv', delimiter=',', skip_header=1)
            x[:,i] = 2 * np.pi * self.radii[i]*1e-9 / wavelength
            x[:,i] *= m_diel.real
            m[:,i] = df[:,1] + df[:,2]*1j
            m[:,i] /= m_diel.real


        # Calculation using Mie Theory
        _, self.q_ext, self.q_sca, self.q_abs, _, _, _, _, _, _ = scattnlay(x, m)
        
    def normalise(self, mode='ind'):
        # Normalise output cross-sections between 0 and 255
        if mode == 'ind':
            # Individually normalise each cross-section
            MAX_QEXT = np.max(self.q_ext)
            MIN_QEXT = np.min(self.q_ext)

            MAX_QSCA = np.max(self.q_sca)
            MIN_QSCA = np.min(self.q_sca)

            MAX_QABS = np.max(self.q_abs)
            MIN_QABS = np.min(self.q_abs)

        if mode == 'all':
            # Normalise cross-sections by a "global" minimum and maximum
            MAX_Q = np.max((self.q_ext, self.q_sca, self.q_abs))
            MIN_Q = np.min((self.q_ext, self.q_sca, self.q_abs))

            MAX_QEXT = MAX_Q
            MAX_QSCA = MAX_Q
            MAX_QABS = MAX_Q

            MIN_QEXT = MIN_Q
            MIN_QSCA = MIN_Q
            MIN_QABS = MIN_Q

        self.q_ext = np.array((self.q_ext - MIN_QEXT) / (MAX_QEXT - MIN_QEXT) * 255, dtype=np.ubyte)
        self.q_sca = np.array((self.q_sca - MIN_QSCA) / (MAX_QSCA - MIN_QSCA) * 255, dtype=np.ubyte)
        self.q_abs = np.array((self.q_abs - MIN_QABS) / (MAX_QABS - MIN_QABS) * 255, dtype=np.ubyte)
