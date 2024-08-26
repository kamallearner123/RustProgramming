; ModuleID = 'your_program.609fa335a479a42-cgu.0'
source_filename = "your_program.609fa335a479a42-cgu.0"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx11.0.0"

%"core::fmt::rt::Argument<'_>" = type { %"core::fmt::rt::ArgumentType<'_>" }
%"core::fmt::rt::ArgumentType<'_>" = type { [1 x i64], ptr }

@vtable.0 = private unnamed_addr constant <{ ptr, [16 x i8], ptr, ptr, ptr }> <{ ptr @"_ZN4core3ptr85drop_in_place$LT$std..rt..lang_start$LT$$LP$$RP$$GT$..$u7b$$u7b$closure$u7d$$u7d$$GT$17h5c2c5ec977828f40E", [16 x i8] c"\08\00\00\00\00\00\00\00\08\00\00\00\00\00\00\00", ptr @"_ZN4core3ops8function6FnOnce40call_once$u7b$$u7b$vtable.shim$u7d$$u7d$17h43485a37010cc09bE", ptr @"_ZN3std2rt10lang_start28_$u7b$$u7b$closure$u7d$$u7d$17h78fb2a85e88d7576E", ptr @"_ZN3std2rt10lang_start28_$u7b$$u7b$closure$u7d$$u7d$17h78fb2a85e88d7576E" }>, align 8
@0 = private unnamed_addr constant <{ [8 x i8], [8 x i8] }> <{ [8 x i8] zeroinitializer, [8 x i8] undef }>, align 8
@alloc_91c7fa63c3cfeaa3c795652d5cf060e4 = private unnamed_addr constant <{ [12 x i8] }> <{ [12 x i8] c"invalid args" }>, align 1
@alloc_af99043bc04c419363a7f04d23183506 = private unnamed_addr constant <{ ptr, [8 x i8] }> <{ ptr @alloc_91c7fa63c3cfeaa3c795652d5cf060e4, [8 x i8] c"\0C\00\00\00\00\00\00\00" }>, align 8
@alloc_5eda5162209f1be4ab31d6da6b13bdd4 = private unnamed_addr constant <{ [84 x i8] }> <{ [84 x i8] c"/private/tmp/rust-20240717-23270-jygm8n/rustc-1.79.0-src/library/core/src/fmt/mod.rs" }>, align 1
@alloc_a0ce9632f4bd77e2609abfb29b2d4854 = private unnamed_addr constant <{ ptr, [16 x i8] }> <{ ptr @alloc_5eda5162209f1be4ab31d6da6b13bdd4, [16 x i8] c"T\00\00\00\00\00\00\00U\01\00\00\0D\00\00\00" }>, align 8
@alloc_4d3da52a5f2caf0fb4dcb36e189ec41c = private unnamed_addr constant <{ [15 x i8] }> <{ [15 x i8] c"your_program.rs" }>, align 1
@alloc_ad7afa521e9cff191e4db414b3ee48c9 = private unnamed_addr constant <{ ptr, [16 x i8] }> <{ ptr @alloc_4d3da52a5f2caf0fb4dcb36e189ec41c, [16 x i8] c"\0F\00\00\00\00\00\00\00\06\00\00\00\09\00\00\00" }>, align 8
@alloc_d8fbf0dbf866d48836b0eec12ee7dd87 = private unnamed_addr constant <{ [4 x i8] }> <{ [4 x i8] c"c = " }>, align 1
@alloc_49a1e817e911805af64bbc7efb390101 = private unnamed_addr constant <{ [1 x i8] }> <{ [1 x i8] c"\0A" }>, align 1
@alloc_6bcbc7e655974355c9a71891144ec852 = private unnamed_addr constant <{ ptr, [8 x i8], ptr, [8 x i8] }> <{ ptr @alloc_d8fbf0dbf866d48836b0eec12ee7dd87, [8 x i8] c"\04\00\00\00\00\00\00\00", ptr @alloc_49a1e817e911805af64bbc7efb390101, [8 x i8] c"\01\00\00\00\00\00\00\00" }>, align 8

; std::sys_common::backtrace::__rust_begin_short_backtrace
; Function Attrs: noinline uwtable
define internal void @_ZN3std10sys_common9backtrace28__rust_begin_short_backtrace17hf331754379d1c6b7E(ptr %f) unnamed_addr #0 {
start:
; call core::ops::function::FnOnce::call_once
  call void @_ZN4core3ops8function6FnOnce9call_once17h672ddace79821942E(ptr %f)
  call void asm sideeffect "", "~{memory}"(), !srcloc !3
  ret void
}

; std::rt::lang_start
; Function Attrs: uwtable
define hidden i64 @_ZN3std2rt10lang_start17heb8dd83912953aeeE(ptr %main, i64 %argc, ptr %argv, i8 %sigpipe) unnamed_addr #1 {
start:
  %_8 = alloca [8 x i8], align 8
  %_5 = alloca [8 x i8], align 8
  store ptr %main, ptr %_8, align 8
; call std::rt::lang_start_internal
  %0 = call i64 @_ZN3std2rt19lang_start_internal17h07dd9d9140cc1a1eE(ptr align 1 %_8, ptr align 8 @vtable.0, i64 %argc, ptr %argv, i8 %sigpipe)
  store i64 %0, ptr %_5, align 8
  %v = load i64, ptr %_5, align 8
  ret i64 %v
}

; std::rt::lang_start::{{closure}}
; Function Attrs: inlinehint uwtable
define internal i32 @"_ZN3std2rt10lang_start28_$u7b$$u7b$closure$u7d$$u7d$17h78fb2a85e88d7576E"(ptr align 8 %_1) unnamed_addr #2 {
start:
  %self = alloca [1 x i8], align 1
  %_4 = load ptr, ptr %_1, align 8
; call std::sys_common::backtrace::__rust_begin_short_backtrace
  call void @_ZN3std10sys_common9backtrace28__rust_begin_short_backtrace17hf331754379d1c6b7E(ptr %_4)
; call <() as std::process::Termination>::report
  %0 = call i8 @"_ZN54_$LT$$LP$$RP$$u20$as$u20$std..process..Termination$GT$6report17h3ceb092f9a997c88E"()
  store i8 %0, ptr %self, align 1
  %_6 = load i8, ptr %self, align 1
  %_0 = zext i8 %_6 to i32
  ret i32 %_0
}

; core::fmt::Arguments::new_v1
; Function Attrs: inlinehint uwtable
define internal void @_ZN4core3fmt9Arguments6new_v117h65fa59e80c4a5bd3E(ptr sret([48 x i8]) align 8 %_0, ptr align 8 %pieces.0, i64 %pieces.1, ptr align 8 %args.0, i64 %args.1) unnamed_addr #2 {
start:
  %_9 = alloca [48 x i8], align 8
  %_3 = icmp ult i64 %pieces.1, %args.1
  br i1 %_3, label %bb3, label %bb1

bb1:                                              ; preds = %start
  %_7 = add i64 %args.1, 1
  %_6 = icmp ugt i64 %pieces.1, %_7
  br i1 %_6, label %bb2, label %bb4

bb3:                                              ; preds = %bb2, %start
  store ptr @alloc_af99043bc04c419363a7f04d23183506, ptr %_9, align 8
  %0 = getelementptr inbounds i8, ptr %_9, i64 8
  store i64 1, ptr %0, align 8
  %1 = load ptr, ptr @0, align 8
  %2 = load i64, ptr getelementptr inbounds (i8, ptr @0, i64 8), align 8
  %3 = getelementptr inbounds i8, ptr %_9, i64 32
  store ptr %1, ptr %3, align 8
  %4 = getelementptr inbounds i8, ptr %3, i64 8
  store i64 %2, ptr %4, align 8
  %5 = getelementptr inbounds i8, ptr %_9, i64 16
  store ptr inttoptr (i64 8 to ptr), ptr %5, align 8
  %6 = getelementptr inbounds i8, ptr %5, i64 8
  store i64 0, ptr %6, align 8
; call core::panicking::panic_fmt
  call void @_ZN4core9panicking9panic_fmt17h2654bdb61a0a2682E(ptr align 8 %_9, ptr align 8 @alloc_a0ce9632f4bd77e2609abfb29b2d4854) #8
  unreachable

bb4:                                              ; preds = %bb1
  store ptr %pieces.0, ptr %_0, align 8
  %7 = getelementptr inbounds i8, ptr %_0, i64 8
  store i64 %pieces.1, ptr %7, align 8
  %8 = load ptr, ptr @0, align 8
  %9 = load i64, ptr getelementptr inbounds (i8, ptr @0, i64 8), align 8
  %10 = getelementptr inbounds i8, ptr %_0, i64 32
  store ptr %8, ptr %10, align 8
  %11 = getelementptr inbounds i8, ptr %10, i64 8
  store i64 %9, ptr %11, align 8
  %12 = getelementptr inbounds i8, ptr %_0, i64 16
  store ptr %args.0, ptr %12, align 8
  %13 = getelementptr inbounds i8, ptr %12, i64 8
  store i64 %args.1, ptr %13, align 8
  ret void

bb2:                                              ; preds = %bb1
  br label %bb3
}

; core::ops::function::FnOnce::call_once{{vtable.shim}}
; Function Attrs: inlinehint uwtable
define internal i32 @"_ZN4core3ops8function6FnOnce40call_once$u7b$$u7b$vtable.shim$u7d$$u7d$17h43485a37010cc09bE"(ptr %_1) unnamed_addr #2 {
start:
  %_2 = alloca [0 x i8], align 1
  %0 = load ptr, ptr %_1, align 8
; call core::ops::function::FnOnce::call_once
  %_0 = call i32 @_ZN4core3ops8function6FnOnce9call_once17h36686bc2e7de0c65E(ptr %0)
  ret i32 %_0
}

; core::ops::function::FnOnce::call_once
; Function Attrs: inlinehint uwtable
define internal i32 @_ZN4core3ops8function6FnOnce9call_once17h36686bc2e7de0c65E(ptr %0) unnamed_addr #2 personality ptr @rust_eh_personality {
start:
  %1 = alloca [16 x i8], align 8
  %_2 = alloca [0 x i8], align 1
  %_1 = alloca [8 x i8], align 8
  store ptr %0, ptr %_1, align 8
; invoke std::rt::lang_start::{{closure}}
  %_0 = invoke i32 @"_ZN3std2rt10lang_start28_$u7b$$u7b$closure$u7d$$u7d$17h78fb2a85e88d7576E"(ptr align 8 %_1)
          to label %bb1 unwind label %cleanup

bb3:                                              ; preds = %cleanup
  %2 = load ptr, ptr %1, align 8
  %3 = getelementptr inbounds i8, ptr %1, i64 8
  %4 = load i32, ptr %3, align 8
  %5 = insertvalue { ptr, i32 } poison, ptr %2, 0
  %6 = insertvalue { ptr, i32 } %5, i32 %4, 1
  resume { ptr, i32 } %6

cleanup:                                          ; preds = %start
  %7 = landingpad { ptr, i32 }
          cleanup
  %8 = extractvalue { ptr, i32 } %7, 0
  %9 = extractvalue { ptr, i32 } %7, 1
  store ptr %8, ptr %1, align 8
  %10 = getelementptr inbounds i8, ptr %1, i64 8
  store i32 %9, ptr %10, align 8
  br label %bb3

bb1:                                              ; preds = %start
  ret i32 %_0
}

; core::ops::function::FnOnce::call_once
; Function Attrs: inlinehint uwtable
define internal void @_ZN4core3ops8function6FnOnce9call_once17h672ddace79821942E(ptr %_1) unnamed_addr #2 {
start:
  %_2 = alloca [0 x i8], align 1
  call void %_1()
  ret void
}

; core::ptr::drop_in_place<std::rt::lang_start<()>::{{closure}}>
; Function Attrs: inlinehint uwtable
define internal void @"_ZN4core3ptr85drop_in_place$LT$std..rt..lang_start$LT$$LP$$RP$$GT$..$u7b$$u7b$closure$u7d$$u7d$$GT$17h5c2c5ec977828f40E"(ptr align 8 %_1) unnamed_addr #2 {
start:
  ret void
}

; <() as std::process::Termination>::report
; Function Attrs: inlinehint uwtable
define internal i8 @"_ZN54_$LT$$LP$$RP$$u20$as$u20$std..process..Termination$GT$6report17h3ceb092f9a997c88E"() unnamed_addr #2 {
start:
  ret i8 0
}

; your_program::main
; Function Attrs: uwtable
define internal void @_ZN12your_program4main17h5f9d21ed2edec2f6E() unnamed_addr #1 {
start:
  %_3.i = alloca [16 x i8], align 8
  %_11 = alloca [16 x i8], align 8
  %_10 = alloca [16 x i8], align 8
  %_6 = alloca [48 x i8], align 8
  %c = alloca [4 x i8], align 4
  %0 = call { i32, i1 } @llvm.sadd.with.overflow.i32(i32 10, i32 20)
  %_4.0 = extractvalue { i32, i1 } %0, 0
  %_4.1 = extractvalue { i32, i1 } %0, 1
  %1 = call i1 @llvm.expect.i1(i1 %_4.1, i1 false)
  br i1 %1, label %panic, label %bb1

bb1:                                              ; preds = %start
  store i32 %_4.0, ptr %c, align 4
  store ptr %c, ptr %_3.i, align 8
  %2 = getelementptr inbounds i8, ptr %_3.i, i64 8
  store ptr @"_ZN4core3fmt3num3imp52_$LT$impl$u20$core..fmt..Display$u20$for$u20$i32$GT$3fmt17h2b27c4363ed6d6e6E", ptr %2, align 8
  call void @llvm.memcpy.p0.p0.i64(ptr align 8 %_11, ptr align 8 %_3.i, i64 16, i1 false)
  %3 = getelementptr inbounds [1 x %"core::fmt::rt::Argument<'_>"], ptr %_10, i64 0, i64 0
  call void @llvm.memcpy.p0.p0.i64(ptr align 8 %3, ptr align 8 %_11, i64 16, i1 false)
; call core::fmt::Arguments::new_v1
  call void @_ZN4core3fmt9Arguments6new_v117h65fa59e80c4a5bd3E(ptr sret([48 x i8]) align 8 %_6, ptr align 8 @alloc_6bcbc7e655974355c9a71891144ec852, i64 2, ptr align 8 %_10, i64 1)
; call std::io::stdio::_print
  call void @_ZN3std2io5stdio6_print17h299f38bb21490c1fE(ptr align 8 %_6)
  ret void

panic:                                            ; preds = %start
; call core::panicking::panic_const::panic_const_add_overflow
  call void @_ZN4core9panicking11panic_const24panic_const_add_overflow17h850d076b5415977aE(ptr align 8 @alloc_ad7afa521e9cff191e4db414b3ee48c9) #8
  unreachable
}

; std::rt::lang_start_internal
; Function Attrs: uwtable
declare i64 @_ZN3std2rt19lang_start_internal17h07dd9d9140cc1a1eE(ptr align 1, ptr align 8, i64, ptr, i8) unnamed_addr #1

; core::fmt::num::imp::<impl core::fmt::Display for i32>::fmt
; Function Attrs: uwtable
declare zeroext i1 @"_ZN4core3fmt3num3imp52_$LT$impl$u20$core..fmt..Display$u20$for$u20$i32$GT$3fmt17h2b27c4363ed6d6e6E"(ptr align 4, ptr align 8) unnamed_addr #1

; Function Attrs: nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i64(ptr noalias nocapture writeonly, ptr noalias nocapture readonly, i64, i1 immarg) #3

; core::panicking::panic_fmt
; Function Attrs: cold noinline noreturn uwtable
declare void @_ZN4core9panicking9panic_fmt17h2654bdb61a0a2682E(ptr align 8, ptr align 8) unnamed_addr #4

; Function Attrs: uwtable
declare i32 @rust_eh_personality(i32, i32, i64, ptr, ptr) unnamed_addr #1

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare { i32, i1 } @llvm.sadd.with.overflow.i32(i32, i32) #5

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(none)
declare i1 @llvm.expect.i1(i1, i1) #6

; core::panicking::panic_const::panic_const_add_overflow
; Function Attrs: cold noinline noreturn uwtable
declare void @_ZN4core9panicking11panic_const24panic_const_add_overflow17h850d076b5415977aE(ptr align 8) unnamed_addr #4

; std::io::stdio::_print
; Function Attrs: uwtable
declare void @_ZN3std2io5stdio6_print17h299f38bb21490c1fE(ptr align 8) unnamed_addr #1

define i32 @main(i32 %0, ptr %1) unnamed_addr #7 {
top:
  %2 = sext i32 %0 to i64
; call std::rt::lang_start
  %3 = call i64 @_ZN3std2rt10lang_start17heb8dd83912953aeeE(ptr @_ZN12your_program4main17h5f9d21ed2edec2f6E, i64 %2, ptr %1, i8 0)
  %4 = trunc i64 %3 to i32
  ret i32 %4
}

attributes #0 = { noinline uwtable "frame-pointer"="non-leaf" "probe-stack"="inline-asm" "target-cpu"="apple-m1" }
attributes #1 = { uwtable "frame-pointer"="non-leaf" "probe-stack"="inline-asm" "target-cpu"="apple-m1" }
attributes #2 = { inlinehint uwtable "frame-pointer"="non-leaf" "probe-stack"="inline-asm" "target-cpu"="apple-m1" }
attributes #3 = { nocallback nofree nounwind willreturn memory(argmem: readwrite) }
attributes #4 = { cold noinline noreturn uwtable "frame-pointer"="non-leaf" "probe-stack"="inline-asm" "target-cpu"="apple-m1" }
attributes #5 = { nocallback nofree nosync nounwind speculatable willreturn memory(none) }
attributes #6 = { nocallback nofree nosync nounwind willreturn memory(none) }
attributes #7 = { "frame-pointer"="non-leaf" "target-cpu"="apple-m1" }
attributes #8 = { noreturn }

!llvm.module.flags = !{!0, !1}
!llvm.ident = !{!2}

!0 = !{i32 8, !"PIC Level", i32 2}
!1 = !{i32 7, !"PIE Level", i32 2}
!2 = !{!"rustc version 1.79.0 (129f3b996 2024-06-10) (Homebrew)"}
!3 = !{i32 1697669}
