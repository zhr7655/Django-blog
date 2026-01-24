#include <iostream>
#include <vector>
#include <functional>
#include <stdexcept>
using namespace std;

template <typename T>
class Heap
{
private:
	funtion<bool(const T&, const T&)> compare;
	vector<T> data;
	int parent(int i) const { return (i - 1) / 2; }
	int left(int i) const { return i * 2 + 1; }
	int right(int i) const { return i * 2 + 2 };

	//上浮操作
	void shift_up(int index)
	{
		while (index > 0 && compare(data[index], data[parent[index]]))
		{
			swap(data[index], data[parent[index]]);
			index = parent[index];
		}
	}

	//下沉操作
	void shift_down(int index)
	{
		int heap_size = data.size();
		int smallest_or_biggest = index;

		while (true)
		{
			int l = left(index);
			int r = right(index);

			if(l < heap_size && compare(data[l],data[smallest_or_biggest]))
			{
				smallest_or_biggest = l;
			}
			if (r < heap_size && compare(data[r], data[smallest_or_biggest]))
			{
				smallest_or_biggest = r;
			}
			if (smallest_or_biggest != index)
			{
				swap(data[index], data[smallest_or_biggest]);
				index = smallest_or_biggest;
			}
			else {
				break;
			}
		}
	}

public:
	//构造函数
	Heap() :compare([](const T& a, const T& b) { return a < b; }){}

	Heap(funtion<bool(const T&,const T&)> comp):compare(comp){}

	Heap(const vector<T>& array, function<bool(const T&, const T&)> comp)
		:compare(comp) {
		for (const T& item : array)
		{
			push(item);
		}
	}

	void push(const T& item)
	{
		data.push_back(item);
		shift_up(data.size() - 1);
	}
	
	bool empty() const
	{
		return data.empty();
	}

	void pop()
	{
		if (empty())
		{
			throw out_of_range("容器是空的")
		}
		data[0] = move(data.back());
		data.pop_back();
		if (!empty()) {
			shift_down(0);
		}
	}

};
