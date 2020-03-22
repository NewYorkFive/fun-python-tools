//
//  UIColor+DLColor.m
//
//  Created by NowOrNever on 12/01/2017.
//  Copyright © 2017 NowOrNever. All rights reserved.
//

#import "UIColor+DLColor.h"

@implementation UIColor (DLColor)
+ (instancetype)dl_colorWithHex:(unsigned int) hex{
    int red     = (hex & 0xff0000) >> 16;
    int green   = (hex & 0x00ff00) >> 8;
    int blue    = (hex & 0x0000ff);
    return [UIColor colorWithRed:red/255.0 green:green/255.0 blue:blue/255.0 alpha:1];
}

+ (instancetype)dl_randomColor{
    return [UIColor colorWithRed:arc4random_uniform(256)/255.0 green:arc4random_uniform(256)/255.0 blue:arc4random_uniform(256)/255.0 alpha:1];
}

+ (instancetype)dl_randomColorWithAlpha:(double)alpha{
    return [UIColor colorWithRed:arc4random_uniform(256)/255.0 green:arc4random_uniform(256)/255.0 blue:arc4random_uniform(256)/255.0 alpha:alpha];
}
@end
