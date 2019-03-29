/*
����ģʽ��һ����ֻ��ӵ��һ��ʵ��
*/
#include <iostream>
#include <string>
using namespace std;

class Singleton
{
public:

	static Singleton* GetInstance()
	{
		if (NULL == singleton_)
		{
			singleton_ = new Singleton();
		}
		return singleton_;
	}

private:

	static Singleton* singleton_;
};

Singleton* Singleton::singleton_ = NULL;

class SingletonMultiThread
{
public:
	static SingletonMultiThread* GetInstance()
	{
		if (NULL == singleton_)
		{
			/*TODO:ͬ��*/
			if (NULL == singleton_)
			{
				singleton_ = new SingletonMultiThread();
			}
		}

		return singleton_;
	}

private:
	static SingletonMultiThread* singleton_;
};

SingletonMultiThread* SingletonMultiThread::singleton_ = NULL;

int main()
{
	system("pause");
	return 0;
}
