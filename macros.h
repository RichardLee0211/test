#ifndef _MACROS_H
#define _MACROS_H

#include<math.h> /* for log() function */
#include"global.h"

/* Bit positions */
#define VALID			0
#define DIRTY			1
#define USED			2

/* bit corresponds to the bit number in flags. Least significant bit is 0 */
#define BIT_MASK(n)	1<<(n)
#define IS_SET(flags,bit)	(((flags) & (BIT_MASK(bit)))==0 ? 0 : 1)
#define SET_BIT(flags,bit)	((flags)  |= (BIT_MASK(bit)))
#define CLEAR_BIT(flags,bit) ((flags) &= ~(BIT_MASK(bit)))


#define LOG_PAGE_SIZE (log2(page_size))
#define OFFSET_MASK ((1<<((int)LOG_PAGE_SIZE))-1)

/* Get the page number and page offset from a virtual address. */
#define VADDR_PAGENUM(addr) addr>>((int)LOG_PAGE_SIZE)
#define VADDR_OFFSET(addr) addr & (OFFSET_MASK)

#endif
