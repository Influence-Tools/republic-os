---
type: Jurisdiction
title: "Tyler County, WV"
classification: county
fips: "54095"
state: "WV"
demographics:
  population: 8064
  population_under_18: 1561
  population_18_64: 4548
  population_65_plus: 1955
  median_household_income: 63693
  poverty_rate: 20.21
  homeownership_rate: 84.07
  unemployment_rate: 6.97
  median_home_value: 121300
  gini_index: 0.4853
  vacancy_rate: 19.81
  race_white: 7579
  race_black: 71
  race_asian: 0
  race_native: 6
  hispanic: 88
  bachelors_plus: 1308
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wv/districts/senate/2"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/9"
    rel: in-district
    area_weight: 0.5308
  - to: "us/states/wv/districts/house/8"
    rel: in-district
    area_weight: 0.469
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Tyler County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8064 |
| Under 18 | 1561 |
| 18–64 | 4548 |
| 65+ | 1955 |
| Median household income | 63693 |
| Poverty rate | 20.21 |
| Homeownership rate | 84.07 |
| Unemployment rate | 6.97 |
| Median home value | 121300 |
| Gini index | 0.4853 |
| Vacancy rate | 19.81 |
| White | 7579 |
| Black | 71 |
| Asian | 0 |
| Native | 6 |
| Hispanic/Latino | 88 |
| Bachelor's or higher | 1308 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 2](/us/states/wv/districts/senate/2.md) — 100% (state senate)
- [WV House District 9](/us/states/wv/districts/house/9.md) — 53% (state house)
- [WV House District 8](/us/states/wv/districts/house/8.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
