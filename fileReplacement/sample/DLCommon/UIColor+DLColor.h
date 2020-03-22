//
//  UIColor+DLColor.h
//
//  Created by NowOrNever on 12/01/2017.
//  Copyright © 2017 NowOrNever. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface UIColor (DLColor)
+ (instancetype)dl_colorWithHex:(unsigned int) hex;
+ (instancetype)dl_randomColor;
+ (instancetype)dl_randomColorWithAlpha:(double)alpha;
@end
