##This is for ruby get API test method sample

require 'minitest/autorun'
require 'rest_client'
require 'json'

class TestGETMethods < MiniTest::Unit::TestCase
	def setup
		@response = RestClient.get("http://jsonplaceholder.typicode.com/posts/1")
	end

	def test_check_userid
		data = JSON.parse @response.body
		print data['userId']
		assert_equal(data['userId'], 1,"Should Equal 1")
	end

	def test_check_id
		data = JSON.parse @response.body
		print data['id']
		assert_equal(data['id'], 2,"Should Equal 1")
	end
end