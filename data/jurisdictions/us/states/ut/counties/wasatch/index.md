---
type: Jurisdiction
title: "Wasatch County, UT"
classification: county
fips: "49051"
state: "UT"
demographics:
  population: 36642
  population_under_18: 10559
  population_18_64: 21114
  population_65_plus: 4969
  median_household_income: 117608
  poverty_rate: 4.75
  homeownership_rate: 80.26
  unemployment_rate: 2.02
  median_home_value: 787300
  gini_index: 0.4686
  vacancy_rate: 20.63
  race_white: 30407
  race_black: 65
  race_asian: 394
  race_native: 98
  hispanic: 5387
  bachelors_plus: 16026
districts:
  - to: "us/states/ut/districts/03"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ut/districts/senate/20"
    rel: in-district
    area_weight: 0.8051
  - to: "us/states/ut/districts/senate/26"
    rel: in-district
    area_weight: 0.1457
  - to: "us/states/ut/districts/senate/24"
    rel: in-district
    area_weight: 0.0492
  - to: "us/states/ut/districts/house/59"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Wasatch County, UT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36642 |
| Under 18 | 10559 |
| 18–64 | 21114 |
| 65+ | 4969 |
| Median household income | 117608 |
| Poverty rate | 4.75 |
| Homeownership rate | 80.26 |
| Unemployment rate | 2.02 |
| Median home value | 787300 |
| Gini index | 0.4686 |
| Vacancy rate | 20.63 |
| White | 30407 |
| Black | 65 |
| Asian | 394 |
| Native | 98 |
| Hispanic/Latino | 5387 |
| Bachelor's or higher | 16026 |

## Districts

- [UT-03](/us/states/ut/districts/03.md) — 100% (congressional)
- [UT Senate District 20](/us/states/ut/districts/senate/20.md) — 81% (state senate)
- [UT Senate District 26](/us/states/ut/districts/senate/26.md) — 15% (state senate)
- [UT Senate District 24](/us/states/ut/districts/senate/24.md) — 5% (state senate)
- [UT House District 59](/us/states/ut/districts/house/59.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
