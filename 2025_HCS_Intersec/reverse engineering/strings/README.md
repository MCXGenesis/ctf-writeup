# strings
>  Soal yang wajib ada di CTF pemerintah

## The challenge

Given a file `strings` without any file extension

## How to solve?

The first step to analyze this kind of file is to do `strings` on the terminal (instructed by the challenge's title). Let's see the results.

```
➜ strings strings         
/lib64/ld-linux-x86-64.so.2
__libc_start_main
__cxa_finalize
libc.so.6
GLIBC_2.2.5
GLIBC_2.34
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u+UH
HCS{ctf_
gjls_
hadiah_el
it__
ayaya}
;*3$"
GCC: (Debian 12.2.0-14+deb12u1) 12.2.0
Scrt1.o
__abi_tag
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.0
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
main.c
__FRAME_END__
_DYNAMIC
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_start_main@GLIBC_2.34
_ITM_deregisterTMCloneTable
_edata
_fini
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
_end
__bss_start
main
__TMC_END__
_ITM_registerTMCloneTable
hihi
__cxa_finalize@GLIBC_2.2.5
_init
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.got.plt
.data
.bss
.comment

```
Welp, its pretty obvious. I can already see the flag on the 12th line. Its 

```
HCS{ctf_
gjls_
hadiah_el
it__
ayaya}
```
After making it into one line, I got the flag to submit.

## Flag
```
HCS{ctf_gjls_hadiah_elit__ayaya}
```