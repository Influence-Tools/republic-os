---
type: Jurisdiction
title: "Logan County, WV"
classification: county
fips: "54045"
state: "WV"
demographics:
  population: 31418
  population_under_18: 6528
  population_18_64: 17844
  population_65_plus: 7046
  median_household_income: 49723
  poverty_rate: 21.78
  homeownership_rate: 77.05
  unemployment_rate: 8.51
  median_home_value: 103400
  gini_index: 0.5092
  vacancy_rate: 13.62
  race_white: 30048
  race_black: 616
  race_asian: 79
  race_native: 2
  hispanic: 258
  bachelors_plus: 4843
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/7"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wv/districts/house/33"
    rel: in-district
    area_weight: 0.5104
  - to: "us/states/wv/districts/house/31"
    rel: in-district
    area_weight: 0.4888
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Logan County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31418 |
| Under 18 | 6528 |
| 18–64 | 17844 |
| 65+ | 7046 |
| Median household income | 49723 |
| Poverty rate | 21.78 |
| Homeownership rate | 77.05 |
| Unemployment rate | 8.51 |
| Median home value | 103400 |
| Gini index | 0.5092 |
| Vacancy rate | 13.62 |
| White | 30048 |
| Black | 616 |
| Asian | 79 |
| Native | 2 |
| Hispanic/Latino | 258 |
| Bachelor's or higher | 4843 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 7](/us/states/wv/districts/senate/7.md) — 100% (state senate)
- [WV House District 33](/us/states/wv/districts/house/33.md) — 51% (state house)
- [WV House District 31](/us/states/wv/districts/house/31.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
