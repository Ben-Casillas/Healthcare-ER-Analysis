#rejected records
# Test                                   Expected result
# One invalid record	                Appears in rejection report
# One record fails multiple checks	    Appears once with multiple reasons
# No invalid records	                 Empty rejection report
# Every rejected record	                  Has a rejection reason
# Two records have duplicate IDs	    Both remain distinguishable
# Missing record ID	                    Record still appears in report

#summary
# No rejected records	                     0% failure
# All records rejected	                        100% failure
# 3 of 100 rejected	                            3% failure
# Multiple validation failures on one record	Record counted once
# Empty DataFrame	                            0 records, 0% failure