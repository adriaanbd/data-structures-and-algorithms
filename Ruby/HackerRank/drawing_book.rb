class Page
	attr_reader :page_num
	attr_accessor :left, :right

	def initialize(page_num, left=nil, right=nil)
		@page_num = page_num 
		@left = left 
		@right = right
	end 
end

class Book 
	attr_accessor :pages, :head, :tail

	def initialize(pages)
		@pages = pages 
		@book = []

	def create_page(num)
		@page = Page.new()
		@page
	end	

end