#!/usr/bin/env ruby
Data = ARGV[0].scan(/from:(.*?)\]|to:(.*?)\]|flags:(.*?)\]/)
CompactedData = Data.map { |sub_array| sub_array.compact }
puts CompactedData.join(',')
