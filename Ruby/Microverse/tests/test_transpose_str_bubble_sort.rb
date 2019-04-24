require 'minitest/autorun'
load './transpose_str_bubble_sort.rb'

class TransposeStrBubbleSortTest < MiniTest::Test
  def test_single_swap
    string = 'he was searchign on Bign for signign kigns'
    assert_equal('he was searching on Bing for singing kings', transpose(string))
  end

  def test_swap_over_two_chars
    string = 'rignadingdiggn!'
    assert_equal('ringadingdingg!', transpose(string))
  end

  def test_multiple_char_swap
    string= 'gngngnnggnngggnnn'
    assert_equal('nnnnnnnnngggggggg', transpose(string))
  end
end