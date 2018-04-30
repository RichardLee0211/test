/* this is from the C++ template mateprograming concept tools and techniques
 * from boost and beyond.pdf
 */

template<typename ForwardIterator1, typename ForwardIterator2>
void iter_swap(ForwardIterator1 i1, ForwardIterator2 i2){
    typename ForwardIterator1::value_type tmp = *i1;
    *i1 = *i2;
    *i2 = tmp;
}
