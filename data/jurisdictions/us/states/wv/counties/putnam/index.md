---
type: Jurisdiction
title: "Putnam County, WV"
classification: county
fips: "54079"
state: "WV"
demographics:
  population: 57177
  population_under_18: 12295
  population_18_64: 33627
  population_65_plus: 11255
  median_household_income: 79527
  poverty_rate: 10.59
  homeownership_rate: 81.78
  unemployment_rate: 3.11
  median_home_value: 223300
  gini_index: 0.4316
  vacancy_rate: 6.86
  race_white: 53747
  race_black: 542
  race_asian: 458
  race_native: 32
  hispanic: 871
  bachelors_plus: 16346
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/4"
    rel: in-district
    area_weight: 0.5427
  - to: "us/states/wv/districts/senate/8"
    rel: in-district
    area_weight: 0.4572
  - to: "us/states/wv/districts/house/19"
    rel: in-district
    area_weight: 0.4858
  - to: "us/states/wv/districts/house/21"
    rel: in-district
    area_weight: 0.2991
  - to: "us/states/wv/districts/house/20"
    rel: in-district
    area_weight: 0.1401
  - to: "us/states/wv/districts/house/18"
    rel: in-district
    area_weight: 0.0748
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Putnam County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 57177 |
| Under 18 | 12295 |
| 18–64 | 33627 |
| 65+ | 11255 |
| Median household income | 79527 |
| Poverty rate | 10.59 |
| Homeownership rate | 81.78 |
| Unemployment rate | 3.11 |
| Median home value | 223300 |
| Gini index | 0.4316 |
| Vacancy rate | 6.86 |
| White | 53747 |
| Black | 542 |
| Asian | 458 |
| Native | 32 |
| Hispanic/Latino | 871 |
| Bachelor's or higher | 16346 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 4](/us/states/wv/districts/senate/4.md) — 54% (state senate)
- [WV Senate District 8](/us/states/wv/districts/senate/8.md) — 46% (state senate)
- [WV House District 19](/us/states/wv/districts/house/19.md) — 49% (state house)
- [WV House District 21](/us/states/wv/districts/house/21.md) — 30% (state house)
- [WV House District 20](/us/states/wv/districts/house/20.md) — 14% (state house)
- [WV House District 18](/us/states/wv/districts/house/18.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
