require 'minitest/autorun'
load './balanced_brackets.rb'

class BalancedBracketsTest < MiniTest::Test
  def test_get_brackets
    actual = get_brackets('(hello)[world]')
    expected = '(', ')', '[', ']'
    assert_equal(actual, expected)

    actual = get_brackets('[({}{}{})([])]')
    expected = '[', '(', '{', '}', '{', '}', '{', '}', ')', '(', '[', ']', ')', ']'
    assert_equal(actual, expected)
  end

  def test_get_brackets_is_empty
    actual = get_brackets('hello world')
    assert_equal([], actual)
  end

  def test_balanced_brackets_is_empty
    assert_equal(false, balanced_brackets?('hello world'))
  end

end