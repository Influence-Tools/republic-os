---
type: Jurisdiction
title: "Jackson County, WV"
classification: county
fips: "54035"
state: "WV"
demographics:
  population: 27705
  population_under_18: 5942
  population_18_64: 15876
  population_65_plus: 5887
  median_household_income: 58845
  poverty_rate: 18.45
  homeownership_rate: 78.65
  unemployment_rate: 5.15
  median_home_value: 157200
  gini_index: 0.4941
  vacancy_rate: 10.51
  race_white: 26567
  race_black: 39
  race_asian: 110
  race_native: 7
  hispanic: 292
  bachelors_plus: 5591
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wv/districts/senate/4"
    rel: in-district
    area_weight: 0.5435
  - to: "us/states/wv/districts/senate/8"
    rel: in-district
    area_weight: 0.4563
  - to: "us/states/wv/districts/house/16"
    rel: in-district
    area_weight: 0.7798
  - to: "us/states/wv/districts/house/17"
    rel: in-district
    area_weight: 0.22
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Jackson County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27705 |
| Under 18 | 5942 |
| 18–64 | 15876 |
| 65+ | 5887 |
| Median household income | 58845 |
| Poverty rate | 18.45 |
| Homeownership rate | 78.65 |
| Unemployment rate | 5.15 |
| Median home value | 157200 |
| Gini index | 0.4941 |
| Vacancy rate | 10.51 |
| White | 26567 |
| Black | 39 |
| Asian | 110 |
| Native | 7 |
| Hispanic/Latino | 292 |
| Bachelor's or higher | 5591 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 4](/us/states/wv/districts/senate/4.md) — 54% (state senate)
- [WV Senate District 8](/us/states/wv/districts/senate/8.md) — 46% (state senate)
- [WV House District 16](/us/states/wv/districts/house/16.md) — 78% (state house)
- [WV House District 17](/us/states/wv/districts/house/17.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
