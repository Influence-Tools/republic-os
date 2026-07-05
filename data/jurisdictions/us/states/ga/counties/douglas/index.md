---
type: Jurisdiction
title: "Douglas County, GA"
classification: county
fips: "13097"
state: "GA"
demographics:
  population: 147888
  population_under_18: 37449
  population_18_64: 92388
  population_65_plus: 18051
  median_household_income: 82984
  poverty_rate: 10.86
  homeownership_rate: 66.92
  unemployment_rate: 6.22
  median_home_value: 296900
  gini_index: 0.4198
  vacancy_rate: 7.31
  race_white: 48708
  race_black: 74289
  race_asian: 2627
  race_native: 548
  hispanic: 18079
  bachelors_plus: 41486
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.5398
  - to: "us/states/ga/districts/06"
    rel: in-district
    area_weight: 0.4596
  - to: "us/states/ga/districts/senate/30"
    rel: in-district
    area_weight: 0.5776
  - to: "us/states/ga/districts/senate/28"
    rel: in-district
    area_weight: 0.4223
  - to: "us/states/ga/districts/house/40"
    rel: in-district
    area_weight: 0.4177
  - to: "us/states/ga/districts/house/64"
    rel: in-district
    area_weight: 0.374
  - to: "us/states/ga/districts/house/66"
    rel: in-district
    area_weight: 0.208
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Douglas County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 147888 |
| Under 18 | 37449 |
| 18–64 | 92388 |
| 65+ | 18051 |
| Median household income | 82984 |
| Poverty rate | 10.86 |
| Homeownership rate | 66.92 |
| Unemployment rate | 6.22 |
| Median home value | 296900 |
| Gini index | 0.4198 |
| Vacancy rate | 7.31 |
| White | 48708 |
| Black | 74289 |
| Asian | 2627 |
| Native | 548 |
| Hispanic/Latino | 18079 |
| Bachelor's or higher | 41486 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 54% (congressional)
- [GA-06](/us/states/ga/districts/06.md) — 46% (congressional)
- [GA Senate District 30](/us/states/ga/districts/senate/30.md) — 58% (state senate)
- [GA Senate District 28](/us/states/ga/districts/senate/28.md) — 42% (state senate)
- [GA House District 40](/us/states/ga/districts/house/40.md) — 42% (state house)
- [GA House District 64](/us/states/ga/districts/house/64.md) — 37% (state house)
- [GA House District 66](/us/states/ga/districts/house/66.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
