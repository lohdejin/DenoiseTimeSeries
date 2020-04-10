import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] =[16,12]

class Denoisefft():
    
    def __init__(self,array,tf,dt):
         
         """
         Denoisefft class for calulating the fft and
         visualizing the Power Spectral Density to identify the
         significant components in the data and using it to denoise the
         time Series
     
         Attributes:
             array (numpy array dtype float) representing the time Series
             data value
             tf (int) final time value of the collected time series
             dt (float) the sample time for time series
         """
         self.arr=array
         self.tf=tf
         self.dt=dt

    def PSD(self):
    
        """
        calculate the fast fourier transform and the Power Spectral
        Density (PSD). Visualizing the time series data & PSD
        Argument:
            none
        return:
            none
        """
        self.t=np.arange(0,self.tf,self.dt)
        self.n=len(self.t)
        self.fhat=np.fft.fft(self.arr,self.n)
        self.PSD=self.fhat * np.conj(self.fhat)/self.n
        self.L=np.arange(1,np.floor(self.n/2),dtype='int')
        self.freq=(1/(self.dt*self.n)) * np.arange(self.n)
       
        fig,axs=plt.subplots(2,1)
        plt.sca(axs[0])
        plt.plot(self.t,self.arr,color='b',LineWidth=1.5,label='Noisy')
        plt.xlim(self.t[0],self.t[-1])
        plt.title('Time Series')
        plt.xlabel('Time (sec)')
        plt.ylabel('Value')
        plt.legend()
       
        plt.sca(axs[1])
        plt.plot(self.freq[self.L],self.PSD[self.L],color='r',LineWidth=2,label='PSD')
        plt.xlim(self.freq[self.L[0]],self.freq[self.L[-1]])
        plt.title('Power Spectral Density')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('PSD')
        plt.legend()
        plt.show()
   
        #plot the histogram of the power spectrum
        plt.boxplot(np.abs(self.PSD))
        plt.title('Amplitude distribution')
        plt.xlabel('Amplitude')
        plt.ylabel('Value Distribution')
        plt.legend()
        plt.show()

    def denoise(self,amp):
        """
            Use the threshold magnitude to filter out the frequencies that whatever
            magnitude lower than threshold.
            Arguments:
                amp (float) the cut off magnitude
            return:
                none
        """
        
        
        self.indices = self.PSD > amp
        self.PSDclean=self.PSD*self.indices
        self.fhatclean=self.indices*self.fhat
        self.ffilt=np.fft.ifft(self.fhatclean)
        
        fig,axs=plt.subplots(3,1)
        plt.sca(axs[0])
        plt.plot(self.t,self.arr,color='b',LineWidth=1.5,label='Noisy')
        plt.xlim(self.t[0],self.t[-1])
        plt.title('Noisy Time Series')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Value')
        plt.legend()
        
        plt.sca(axs[1])
        plt.plot(self.t,self.ffilt,color='k',LineWidth=1.5,label='Clean')
        plt.xlim(self.t[0],self.t[-1])
        plt.title('Clean Time Series')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Value')
        plt.legend()
        
        plt.sca(axs[2])
        plt.plot(self.freq[self.L],self.PSD[self.L],color='r',LineWidth=2,label='PSD')
        plt.xlim(self.freq[self.L[0]],self.freq[self.L[-1]])
        plt.title('Power Spectral Density')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('PSD')
        plt.legend()