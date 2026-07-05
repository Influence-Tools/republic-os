---
type: Jurisdiction
title: "Valley County, MT"
classification: county
fips: "30105"
state: "MT"
demographics:
  population: 7519
  population_under_18: 1679
  population_18_64: 3997
  population_65_plus: 1843
  median_household_income: 71695
  poverty_rate: 10.12
  homeownership_rate: 78.48
  unemployment_rate: 2.98
  median_home_value: 198400
  gini_index: 0.376
  vacancy_rate: 30.63
  race_white: 6356
  race_black: 30
  race_asian: 2
  race_native: 626
  hispanic: 194
  bachelors_plus: 1663
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/16"
    rel: in-district
    area_weight: 0.399
  - to: "us/states/mt/districts/senate/14"
    rel: in-district
    area_weight: 0.3503
  - to: "us/states/mt/districts/senate/15"
    rel: in-district
    area_weight: 0.2505
  - to: "us/states/mt/districts/house/28"
    rel: in-district
    area_weight: 0.3503
  - to: "us/states/mt/districts/house/29"
    rel: in-district
    area_weight: 0.2505
  - to: "us/states/mt/districts/house/31"
    rel: in-district
    area_weight: 0.2183
  - to: "us/states/mt/districts/house/32"
    rel: in-district
    area_weight: 0.1808
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Valley County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7519 |
| Under 18 | 1679 |
| 18–64 | 3997 |
| 65+ | 1843 |
| Median household income | 71695 |
| Poverty rate | 10.12 |
| Homeownership rate | 78.48 |
| Unemployment rate | 2.98 |
| Median home value | 198400 |
| Gini index | 0.376 |
| Vacancy rate | 30.63 |
| White | 6356 |
| Black | 30 |
| Asian | 2 |
| Native | 626 |
| Hispanic/Latino | 194 |
| Bachelor's or higher | 1663 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 16](/us/states/mt/districts/senate/16.md) — 40% (state senate)
- [MT Senate District 14](/us/states/mt/districts/senate/14.md) — 35% (state senate)
- [MT Senate District 15](/us/states/mt/districts/senate/15.md) — 25% (state senate)
- [MT House District 28](/us/states/mt/districts/house/28.md) — 35% (state house)
- [MT House District 29](/us/states/mt/districts/house/29.md) — 25% (state house)
- [MT House District 31](/us/states/mt/districts/house/31.md) — 22% (state house)
- [MT House District 32](/us/states/mt/districts/house/32.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
