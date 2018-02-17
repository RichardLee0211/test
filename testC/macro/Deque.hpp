#ifndef DEQUE_H
#define DEQUE_H
#include <stdio.h>
#include <string.h>
#include <assert.h>


#define INITIAL_CAPACITY 20
#define _DEBUG 0
#define THRESHOLD 0

#define Deque_DEFINE(t)                                                        \
    /* delaration */                                                           \
	struct Deque_##t##_Iterator;                                               \
	struct Deque_##t;                                                          \
                                                                               \
    /* defination */                                                           \
	struct Deque_##t{                                                          \
	};                                                                         \
                                                                               \
	struct Deque_##t##_Iterator{                                               \
		int current;                                                           \
		Deque_##t *dp;                                                         \
        /* function pointers */                                                \
		void (*inc)(Deque_##t##_Iterator *it);                                 \
		void (*dec)(Deque_##t##_Iterator *it);                                 \
		t& (*deref)(Deque_##t##_Iterator *it);                                 \
	};                                                                         \
                                                                               \
    /* Iterator functions */                                                   \
	void Deque_##t##_Iterator_inc(Deque_##t##_Iterator *it){                   \
		it->current=(it->current+1) % (it->dp->capacity);                      \
	}                                                                          \
	void Deque_##t##_Iterator_dec(Deque_##t##_Iterator *it){                   \
		it->current=(it->current+it->dp->capacity-1) % (it->dp->capacity);     \
	}                                                                          \
	t& Deque_##t##_Iterator_deref(Deque_##t##_Iterator *it1){                  \
		return it1->dp->data[it1->current];                                    \
	}                                                                          \
                                                                               \
    /* t functions */                                                          \
	Deque_##t##_Iterator Deque_##t##_begin(Deque_##t *dp){                     \
		Deque_##t##_Iterator it;                                               \
		it.current=dp->head;                                                   \
		it.dp = dp;                                                            \
		it.inc = &Deque_##t##_Iterator_inc;                                    \
		it.dec = &Deque_##t##_Iterator_dec;                                    \
		it.deref = &Deque_##t##_Iterator_deref;                                \
		return it;                                                             \
	}                                                                          \
                                                                               \
    /* point to the one next to last one */                                    \
	Deque_##t##_Iterator Deque_##t##_end(Deque_##t *dp){                       \
		Deque_##t##_Iterator it;                                               \
		it.current=dp->tail;                                                   \
		it.dp = dp;                                                            \
		it.inc = &Deque_##t##_Iterator_inc;                                    \
		it.dec = &Deque_##t##_Iterator_dec;                                    \
		it.deref = &Deque_##t##_Iterator_deref;                                \
		return it;                                                             \
	}                                                                          \
                                                                               \
	bool Deque_##t##_Iterator_equal(Deque_##t##_Iterator it1,                  \
	}                                                                          \
                                                                               \
	void Deque_##t##_clear(Deque_##t *dp){                                     \
	}                                                                          \
                                                                               \
    /* define by test file, as a global function */                            \
    /* TODO: what's equal between two deque, does it require data identical??*/\
	bool Deque_##t##_equal(Deque_##t a , Deque_##t b){                         \
	}                                                                          \
                                                                               \
	t & Deque_##t##_front(Deque_##t *dp){                                      \
		return dp->data[(dp->head)];                                           \
	}                                                                          \
                                                                               \
    /* return the last one, differ from end() -- the one next the last */      \
	t & Deque_##t##_back(Deque_##t *dp){                                       \
		return dp->data[(dp->tail-1) % (dp->capacity)];                        \
	}                                                                          \
                                                                               \
    /* well this at function expect to be a offset of deque front */           \
	t & Deque_##t##_at(Deque_##t *dp, int i){                                  \
	}                                                                          \
	t Deque_##t##_at_retVal(Deque_##t *dp, int i){                             \
	}                                                                          \
                                                                               \
	void double_capacity(Deque_##t *dp){                                       \
	}                                                                          \
                                                                               \
	void Deque_##t##_push_front(Deque_##t *dp, t element){                     \
	}                                                                          \
                                                                               \
	void Deque_##t##_push_back(Deque_##t *dp, t element){                      \
	}                                                                          \
	void Deque_##t##_pop_front(Deque_##t *dp){                                 \
	}                                                                          \
	void Deque_##t##_pop_back(Deque_##t *dp){                                  \
	}                                                                          \
	int Deque_##t##_size(Deque_##t *dp){                                       \
		return dp->sizeCounter;                                                \
	}                                                                          \
	void Deque_##t##_dtor(Deque_##t *dp){                                      \
		free(dp->data);                                                        \
	}                                                                          \
	bool Deque_##t##_isEmpty(Deque_##t *dp){                                   \
		return dp->sizeCounter==0;                                             \
	}                                                                          \
                                                                               \
    /* sort part */                                                            \
    int                                                                        \
    Deque_##t##_findpivoit(Deque_##t* dp,                                      \
    }                                                                          \
    inline void                                                                \
    Deque_##t##_swap(Deque_##t* dp,                                            \
    }                                                                          \
    int                                                                        \
    Deque_##t##_partition(Deque_##t* dp, int l, int r, int pivot){             \
    }                                                                          \
    /**                                                                        \
     * this is a bad API since operate in really dp->data[offset],             \
     * and queue is a loop in data array, make it hard to imply qsort()        \
     */                                                                        \
    void Deque_##t##_sort(Deque_##t *dp,                                       \
    }                                                                          \
                                                                               \
    /* using virtual offset offer by _at function, could be better */          \
    void Deque_##t##_qsort(Deque_##t *dp,                                      \
    }                                                                          \
                                                                               \
    /* constructor, should put in very begining but forward delare issue */    \
	void Deque_##t##_ctor(Deque_##t *dp,                                       \
            bool (*isSorted)(const t& a , const t& b)){                        \
        /* data member initialize */                                           \
		dp->capacity=INITIAL_CAPACITY;                                         \
		dp->data = (t*) malloc(sizeof(t) * dp->capacity);                      \
        dp->head=0;                                                            \
        dp->tail=0;                                                            \
        dp->sizeCounter=0;                                                     \
		strcpy(dp->type_name,"Deque_");                                        \
		strcat(dp->type_name,#t);                                              \
        /* function pointer setter */                                          \
        /* destructor and constroctor */                                       \
        dp->ctor =      &Deque_##t##_ctor;                                     \
		dp->dtor =      &Deque_##t##_dtor;                                     \
        /*  getter */                                                          \
		dp->front =     &Deque_##t##_front;                                    \
		dp->back =      &Deque_##t##_back;                                     \
		dp->at=			&Deque_##t##_at;                                       \
		dp->at_retVal=	&Deque_##t##_at_retVal;                                \
		dp->begin =     &Deque_##t##_begin;                                    \
		dp->end =       &Deque_##t##_end;                                      \
		dp->size =		&Deque_##t##_size;                                     \
        /* modifier */                                                         \
		dp->push_front =&Deque_##t##_push_front;                               \
		dp->push_back = &Deque_##t##_push_back;                                \
		dp->pop_front = &Deque_##t##_pop_front;                                \
		dp->pop_back =  &Deque_##t##_pop_back;                                 \
        /* dp->double_capacity = &double_capacity; */ /* set as global */      \
		dp->clear =     &Deque_##t##_clear;                                    \
        /* sorter functions */                                                 \
        dp->sort =      &Deque_##t##_sort;                                     \
        dp->qsort =     &Deque_##t##_qsort;                                    \
        dp->swap =      &Deque_##t##_swap;                                     \
        dp->partition = &Deque_##t##_partition;                                \
        dp->findpivoit= &Deque_##t##_findpivoit;                               \
        /* helper functions */                                                 \
		dp->isEmpty=      &Deque_##t##_isEmpty;                                \
		dp->empty=      &Deque_##t##_isEmpty;  /* make test API happy */       \
		dp->isSorted = isSorted;                                               \
	}                                                                          \

#endif
