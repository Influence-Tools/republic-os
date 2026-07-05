---
type: Jurisdiction
title: "Lauderdale County, MS"
classification: county
fips: "28075"
state: "MS"
demographics:
  population: 71504
  population_under_18: 16709
  population_18_64: 41454
  population_65_plus: 13341
  median_household_income: 50817
  poverty_rate: 26.32
  homeownership_rate: 65.1
  unemployment_rate: 5.8
  median_home_value: 133300
  gini_index: 0.4879
  vacancy_rate: 14.44
  race_white: 36378
  race_black: 29202
  race_asian: 521
  race_native: 214
  hispanic: 1823
  bachelors_plus: 15932
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/33"
    rel: in-district
    area_weight: 0.7217
  - to: "us/states/ms/districts/senate/32"
    rel: in-district
    area_weight: 0.2068
  - to: "us/states/ms/districts/senate/31"
    rel: in-district
    area_weight: 0.0714
  - to: "us/states/ms/districts/house/81"
    rel: in-district
    area_weight: 0.5256
  - to: "us/states/ms/districts/house/83"
    rel: in-district
    area_weight: 0.2435
  - to: "us/states/ms/districts/house/45"
    rel: in-district
    area_weight: 0.1849
  - to: "us/states/ms/districts/house/82"
    rel: in-district
    area_weight: 0.0459
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Lauderdale County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 71504 |
| Under 18 | 16709 |
| 18–64 | 41454 |
| 65+ | 13341 |
| Median household income | 50817 |
| Poverty rate | 26.32 |
| Homeownership rate | 65.1 |
| Unemployment rate | 5.8 |
| Median home value | 133300 |
| Gini index | 0.4879 |
| Vacancy rate | 14.44 |
| White | 36378 |
| Black | 29202 |
| Asian | 521 |
| Native | 214 |
| Hispanic/Latino | 1823 |
| Bachelor's or higher | 15932 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 33](/us/states/ms/districts/senate/33.md) — 72% (state senate)
- [MS Senate District 32](/us/states/ms/districts/senate/32.md) — 21% (state senate)
- [MS Senate District 31](/us/states/ms/districts/senate/31.md) — 7% (state senate)
- [MS House District 81](/us/states/ms/districts/house/81.md) — 53% (state house)
- [MS House District 83](/us/states/ms/districts/house/83.md) — 24% (state house)
- [MS House District 45](/us/states/ms/districts/house/45.md) — 18% (state house)
- [MS House District 82](/us/states/ms/districts/house/82.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
