class FourDigitYearConverter:
    regex = r'\d{4}'

    def to_pyhton(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value   #정수로 넘어온 값 네자리 문자열로 바꾸겠다


