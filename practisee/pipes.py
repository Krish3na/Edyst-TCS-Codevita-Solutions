inpipes, outpipes, rust_factor = map(int,input().split())
in_pipes=list(map(int,input().split()))
out_pipes=list(map(int,input().split()))

sum_in=sum(in_pipes)
sum_out=sum(out_pipes)

if sum_in > sum_out:
    print(sum_out-sum_in-rust_factor,end='')

elif sum_out==sum_in:
    print('BALANCED',end='')

else:
    if sum_out-sum_in-rust_factor==0:
        print('BALANCED')
    else:
        print(sum_out-sum_in,end='')
