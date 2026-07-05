---
type: Jurisdiction
title: "Weber County, UT"
classification: county
fips: "49057"
state: "UT"
demographics:
  population: 269648
  population_under_18: 71749
  population_18_64: 164430
  population_65_plus: 33469
  median_household_income: 90005
  poverty_rate: 8.09
  homeownership_rate: 74.06
  unemployment_rate: 3.0
  median_home_value: 426700
  gini_index: 0.4
  vacancy_rate: 6.41
  race_white: 223284
  race_black: 3012
  race_asian: 4157
  race_native: 1883
  hispanic: 51905
  bachelors_plus: 64193
districts:
  - to: "us/states/ut/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ut/districts/senate/3"
    rel: in-district
    area_weight: 0.5353
  - to: "us/states/ut/districts/senate/4"
    rel: in-district
    area_weight: 0.3704
  - to: "us/states/ut/districts/senate/5"
    rel: in-district
    area_weight: 0.0941
  - to: "us/states/ut/districts/house/8"
    rel: in-district
    area_weight: 0.5543
  - to: "us/states/ut/districts/house/12"
    rel: in-district
    area_weight: 0.212
  - to: "us/states/ut/districts/house/6"
    rel: in-district
    area_weight: 0.1351
  - to: "us/states/ut/districts/house/9"
    rel: in-district
    area_weight: 0.0344
  - to: "us/states/ut/districts/house/10"
    rel: in-district
    area_weight: 0.0275
  - to: "us/states/ut/districts/house/7"
    rel: in-district
    area_weight: 0.0202
  - to: "us/states/ut/districts/house/11"
    rel: in-district
    area_weight: 0.0162
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Weber County, UT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 269648 |
| Under 18 | 71749 |
| 18–64 | 164430 |
| 65+ | 33469 |
| Median household income | 90005 |
| Poverty rate | 8.09 |
| Homeownership rate | 74.06 |
| Unemployment rate | 3.0 |
| Median home value | 426700 |
| Gini index | 0.4 |
| Vacancy rate | 6.41 |
| White | 223284 |
| Black | 3012 |
| Asian | 4157 |
| Native | 1883 |
| Hispanic/Latino | 51905 |
| Bachelor's or higher | 64193 |

## Districts

- [UT-01](/us/states/ut/districts/01.md) — 100% (congressional)
- [UT Senate District 3](/us/states/ut/districts/senate/3.md) — 54% (state senate)
- [UT Senate District 4](/us/states/ut/districts/senate/4.md) — 37% (state senate)
- [UT Senate District 5](/us/states/ut/districts/senate/5.md) — 9% (state senate)
- [UT House District 8](/us/states/ut/districts/house/8.md) — 55% (state house)
- [UT House District 12](/us/states/ut/districts/house/12.md) — 21% (state house)
- [UT House District 6](/us/states/ut/districts/house/6.md) — 14% (state house)
- [UT House District 9](/us/states/ut/districts/house/9.md) — 3% (state house)
- [UT House District 10](/us/states/ut/districts/house/10.md) — 3% (state house)
- [UT House District 7](/us/states/ut/districts/house/7.md) — 2% (state house)
- [UT House District 11](/us/states/ut/districts/house/11.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
