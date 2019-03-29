/*
����ģʽ���������㷨�壬�ֱ��װ������������֮����Ի����滻��
��ģʽ���㷨�ı仯������ʹ���㷨�Ŀͻ��� 
*/
#include <iostream>
using namespace std;

class QuackBehavior
{
public:
	virtual void Quack() = 0;
};

class FlyBehavior
{
public:
	virtual void Fly() = 0;
};

class Duck
{
public:
	void Swim()
	{
		cout << "All duck can swim.\n";
	};

	virtual void Display() = 0;

	void PerformQuack()
	{
		pQuackBehavior_->Quack();
	}

	void PerformFly()
	{
		pFlyBehavior_->Fly();
	}

	void SetFlyBehavior(FlyBehavior*	pFlyBehavior)
	{
		pFlyBehavior_ = pFlyBehavior;
	}

	void SetQuackBehavior(QuackBehavior*	pQuackBehavior)
	{
		pQuackBehavior_ = pQuackBehavior;
	}

private:
	
	QuackBehavior*	pQuackBehavior_;
	FlyBehavior*	pFlyBehavior_;	
};



class SqueakDuck:public Duck
{
	void Display()
	{
		cout << "This is a squeak duck.\n";
	}
};

class SqueakSquckBehavior:public QuackBehavior
{
public:
	void Quack()
	{
		cout << "zi zi zi ...\n";
	}
};

class SqueakFlyBehavior:public FlyBehavior
{
public:
	void Fly()
	{
		cout << "Can' fly.\n";
	}
};



int main()
{
	Duck* d = new SqueakDuck;

	d->SetFlyBehavior(new SqueakFlyBehavior);
	d->PerformFly();
	
	d->SetQuackBehavior(new SqueakSquckBehavior);
	d->PerformQuack();

	system("pause");
	return 0;
}

