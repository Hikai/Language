#include <iostream>

template <typename T>
class Exam_data
{
private:
	T data;
public:
	Exam_data(T);
	void set_data(T);
	T get_data(void);
};

template <typename T>
Exam_data<T>::Exam_data(T init_data)
{
	data = init_data;
}

template <typename T>
void Exam_data<T>::set_data(T data)
{
	data = data;
}

template <typename T>
T Exam_data<T>::get_data(void)
{
	return data;
}

int main()
{
	Exam_data<int> a(10);
	std::cout << a.get_data() << std::endl;
	a.set_data(10 + 20);
	std::cout << a.get_data() << std::endl;
	Exam_data<double> b(10.01);
	std::cout << b.get_data() << std::endl;
	return 0;
}
