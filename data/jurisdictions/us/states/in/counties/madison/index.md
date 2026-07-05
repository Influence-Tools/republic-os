---
type: Jurisdiction
title: "Madison County, IN"
classification: county
fips: "18095"
state: "IN"
demographics:
  population: 131900
  population_under_18: 28283
  population_18_64: 78807
  population_65_plus: 24810
  median_household_income: 63037
  poverty_rate: 13.37
  homeownership_rate: 70.16
  unemployment_rate: 5.93
  median_home_value: 161300
  gini_index: 0.4379
  vacancy_rate: 9.9
  race_white: 110320
  race_black: 8068
  race_asian: 865
  race_native: 321
  hispanic: 7102
  bachelors_plus: 25405
districts:
  - to: "us/states/in/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/senate/25"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/house/35"
    rel: in-district
    area_weight: 0.4763
  - to: "us/states/in/districts/house/36"
    rel: in-district
    area_weight: 0.2023
  - to: "us/states/in/districts/house/31"
    rel: in-district
    area_weight: 0.1751
  - to: "us/states/in/districts/house/53"
    rel: in-district
    area_weight: 0.0931
  - to: "us/states/in/districts/house/88"
    rel: in-district
    area_weight: 0.0531
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Madison County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 131900 |
| Under 18 | 28283 |
| 18–64 | 78807 |
| 65+ | 24810 |
| Median household income | 63037 |
| Poverty rate | 13.37 |
| Homeownership rate | 70.16 |
| Unemployment rate | 5.93 |
| Median home value | 161300 |
| Gini index | 0.4379 |
| Vacancy rate | 9.9 |
| White | 110320 |
| Black | 8068 |
| Asian | 865 |
| Native | 321 |
| Hispanic/Latino | 7102 |
| Bachelor's or higher | 25405 |

## Districts

- [IN-05](/us/states/in/districts/05.md) — 100% (congressional)
- [IN Senate District 25](/us/states/in/districts/senate/25.md) — 100% (state senate)
- [IN House District 35](/us/states/in/districts/house/35.md) — 48% (state house)
- [IN House District 36](/us/states/in/districts/house/36.md) — 20% (state house)
- [IN House District 31](/us/states/in/districts/house/31.md) — 18% (state house)
- [IN House District 53](/us/states/in/districts/house/53.md) — 9% (state house)
- [IN House District 88](/us/states/in/districts/house/88.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
