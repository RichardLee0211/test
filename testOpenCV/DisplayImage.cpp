#include<stdio.h>
#include<opencv2/opencv.hpp>

using namespace cv;

#if 0
bool cvMatEQ(const cv::Mat& data1, const cv::Mat& data2)
{
    bool success = true;
    // check if is multi dimensional
    if(data1.dims > 2 || data2.dims > 2)
    {
        if( data1.dims != data2.dims || data1.type() != data2.type() )
        {
            return false;
        }
        for(int32t dim = 0; dim < data1.dims; dim++){
            if(data1.size[dim] != data2.size[dim]){
                return false;
            }
        }
    }
    else
    {
        if(data1.size() != data2.size() || data1.channels() != data2.channels() || data1.type() != data2.type()){
            return false;
        }
    }
    int nrOfElements = data1.total()*data1.elemSize1();
    //bytewise comparison of data
    int cnt = 0;
    for(cnt = 0; cnt < nrOfElements && success; cnt++)
    {
        if(data1.data[cnt] != data2.data[cnt]){
            success = false;
        }
    }
    return success;
}
#endif

int main(int argc, char** argv){
    if(argc!=3){
        printf("usage: displayImage.out <Image_Path> <Image_Path>\n");
        return -1;
    }

    Mat image, image2, result;
    image = imread(argv[1], 1);
    image2 = imread(argv[2], 1);
    result = Mat::Mat();

    if(!image.data || !image2.data){
        printf("No image data \n");
        return -1;
    }

    cv::compare(image , image2  , result , cv::CMP_EQ );
    int percentage  = countNonZero(result);
    std::cout<<percentage<<std::endl;

    // namedWindow("Display Image", WINDOW_AUTOSIZE);
    // imshow("Display Image", image);

    // waitKey(0);

    return 0;
}
