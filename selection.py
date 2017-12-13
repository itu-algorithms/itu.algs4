class Selection:
    @staticmethod
    def sort(a):
        _n = len(a)
        for i in range(_n):
            _min = i
            for j in range(i+1, _n):
                if a[j] < a[_min]:
                    _min = j
            a[i], a[_min] = a[_min], a[i]

    @staticmethod
    def sort_with_comparator(a, cmp):
        _n = len(a)
        for i in range(_n):
            _min = i
            for j in range(i + 1, _n):
                if Selection._less(a[j], a[_min], cmp):
                    _min = j
            a[i], a[_min] = a[_min], a[i]

    @staticmethod
    def _less(v, w, cmp):
        return cmp(v, w) < 0
