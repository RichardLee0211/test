	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 13
	.globl	_main
	.p2align	4, 0x90
_main:                                  ## @main
## BB#0:
	pushl	%ebp
	movl	%esp, %ebp
	pushl	%ebx
	pushl	%edi
	pushl	%esi
	subl	$60, %esp
	calll	L0$pb
L0$pb:
	popl	%eax
	leal	L_.str.1-L0$pb(%eax), %ecx
	movl	$0, -16(%ebp)
	movl	$0, -20(%ebp)
	movl	$0, -24(%ebp)
	movl	$0, -28(%ebp)
	movl	$0, -32(%ebp)
	movl	%esp, %edx
	leal	-32(%ebp), %esi
	movl	%esi, 8(%edx)
	leal	-24(%ebp), %esi
	movl	%esi, 4(%edx)
	leal	L_.str-L0$pb(%eax), %esi
	movl	%esi, (%edx)
	movl	%eax, -36(%ebp)         ## 4-byte Spill
	movl	%ecx, -40(%ebp)         ## 4-byte Spill
	calll	_scanf
	movl	-24(%ebp), %ecx
	movl	-20(%ebp), %edx
	movl	-32(%ebp), %esi
	movl	-28(%ebp), %edi
	movl	%esp, %ebx
	movl	%edi, 12(%ebx)
	movl	%esi, 8(%ebx)
	movl	%edx, 4(%ebx)
	movl	%ecx, (%ebx)
	movl	%eax, -44(%ebp)         ## 4-byte Spill
	calll	___udivdi3
	movl	%esp, %ecx
	movl	%edx, 8(%ecx)
	movl	%eax, 4(%ecx)
	movl	-36(%ebp), %eax         ## 4-byte Reload
	leal	L_.str.1-L0$pb(%eax), %edx
	movl	%edx, (%ecx)
	calll	_printf
	xorl	%ecx, %ecx
	movl	%eax, -48(%ebp)         ## 4-byte Spill
	movl	%ecx, %eax
	addl	$60, %esp
	popl	%esi
	popl	%edi
	popl	%ebx
	popl	%ebp
	retl

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"%lld %lld"

L_.str.1:                               ## @.str.1
	.asciz	"64-bit division is %lld\n"


.subsections_via_symbols
