---
type: Jurisdiction
title: "Lewis County, WV"
classification: county
fips: "54041"
state: "WV"
demographics:
  population: 16740
  population_under_18: 3636
  population_18_64: 9576
  population_65_plus: 3528
  median_household_income: 56477
  poverty_rate: 16.12
  homeownership_rate: 72.21
  unemployment_rate: 8.6
  median_home_value: 151800
  gini_index: 0.4912
  vacancy_rate: 15.23
  race_white: 15064
  race_black: 197
  race_asian: 21
  race_native: 19
  hispanic: 232
  bachelors_plus: 2969
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/wv/districts/senate/12"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/64"
    rel: in-district
    area_weight: 0.8278
  - to: "us/states/wv/districts/house/69"
    rel: in-district
    area_weight: 0.1718
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Lewis County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16740 |
| Under 18 | 3636 |
| 18–64 | 9576 |
| 65+ | 3528 |
| Median household income | 56477 |
| Poverty rate | 16.12 |
| Homeownership rate | 72.21 |
| Unemployment rate | 8.6 |
| Median home value | 151800 |
| Gini index | 0.4912 |
| Vacancy rate | 15.23 |
| White | 15064 |
| Black | 197 |
| Asian | 21 |
| Native | 19 |
| Hispanic/Latino | 232 |
| Bachelor's or higher | 2969 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 12](/us/states/wv/districts/senate/12.md) — 100% (state senate)
- [WV House District 64](/us/states/wv/districts/house/64.md) — 83% (state house)
- [WV House District 69](/us/states/wv/districts/house/69.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
