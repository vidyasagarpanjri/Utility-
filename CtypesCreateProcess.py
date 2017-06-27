from ctypes import *
import WindowStructureDataType as WSDT

k32 = windll.kernel32

#Retrieves a pseudo handle for the current process.
#hProcess = k32.GetCurrentProcess()
#print "pseudo handle : "+str(hProcess)

#Creating a process, which runs independently of the creating process

# security note
# create a process using the CreateProcessAsUser or CreateProcessWithLogonW function.
# This allows you to specify the security context of the user account in which the process will execute

#note dont try with "CreateProcess" only i was getting an error.
#CreateProcessA is ASCII version
#CreateProcessW is unicode version 
'''
structure of CreateProcess
BOOL WINAPI CreateProcess(
  _In_opt_    LPCTSTR               lpApplicationName, "The name or path  of the module to be executed"
  _Inout_opt_ LPTSTR                lpCommandLine,
  _In_opt_    LPSECURITY_ATTRIBUTES lpProcessAttributes,
  _In_opt_    LPSECURITY_ATTRIBUTES lpThreadAttributes,
  _In_        BOOL                  bInheritHandles,
  _In_        DWORD                 dwCreationFlags,
  _In_opt_    LPVOID                lpEnvironment,
  _In_opt_    LPCTSTR               lpCurrentDirectory,
  _In_        LPSTARTUPINFO         lpStartupInfo,
  _Out_       LPPROCESS_INFORMATION lpProcessInformation
);
ref:https://msdn.microsoft.com/en-us/library/windows/desktop/ms682425(v=vs.85).aspx
'''
def debug_new_process(ProcessName):
    #ref: https://msdn.microsoft.com/en-us/library/windows/desktop/ms686285(v=vs.85).aspx
    si = WSDT.STARTUPINFO()
    si.dwFlags = 0x1
    si.wShowWindow = 0x0

    si.cb = sizeof(si)
    pi = WSDT.PROCESS_INFORMATION()

    # The calling thread starts and debugs the new process and all child processes created by the new process.
    # It can receive all related debug events using the WaitForDebugEvent function.
    # WSDT.DEBUG_PROCESS
    #ref: https://msdn.microsoft.com/en-us/library/windows/desktop/ms684863(v=vs.85).aspx
    hProcessCP = k32.CreateProcessA(ProcessName,None,None,None,False,WSDT.DEBUG_PROCESS,None,None,byref(si),byref(pi))
    print "hProcessCP : "+str(hProcessCP)
    PID =  pi.dwProcessId
    print "PID"+str(PID)
    print "Thread ID"+str(pi.dwThreadId)
    if hProcessCP:
        print "process started with PID : %d"% PID
    else:
        err= k32.GetLastError()
        print "[*] Error 0x%08x." % err
        
