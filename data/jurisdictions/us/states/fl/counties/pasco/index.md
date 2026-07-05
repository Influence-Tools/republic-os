---
type: Jurisdiction
title: "Pasco County, FL"
classification: county
fips: "12101"
state: "FL"
demographics:
  population: 611444
  population_under_18: 123778
  population_18_64: 353459
  population_65_plus: 134207
  median_household_income: 70492
  poverty_rate: 11.1
  homeownership_rate: 75.72
  unemployment_rate: 4.9
  median_home_value: 300900
  gini_index: 0.4591
  vacancy_rate: 13.13
  race_white: 439280
  race_black: 38840
  race_asian: 20903
  race_native: 2088
  hispanic: 113819
  bachelors_plus: 176649
districts:
  - to: "us/states/fl/districts/12"
    rel: in-district
    area_weight: 0.6099
  - to: "us/states/fl/districts/15"
    rel: in-district
    area_weight: 0.1499
  - to: "us/states/fl/districts/senate/23"
    rel: in-district
    area_weight: 0.5445
  - to: "us/states/fl/districts/senate/21"
    rel: in-district
    area_weight: 0.1371
  - to: "us/states/fl/districts/senate/11"
    rel: in-district
    area_weight: 0.0741
  - to: "us/states/fl/districts/house/54"
    rel: in-district
    area_weight: 0.3342
  - to: "us/states/fl/districts/house/55"
    rel: in-district
    area_weight: 0.3045
  - to: "us/states/fl/districts/house/56"
    rel: in-district
    area_weight: 0.0614
  - to: "us/states/fl/districts/house/53"
    rel: in-district
    area_weight: 0.0555
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Pasco County, FL

County jurisdiction — 47 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 611444 |
| Under 18 | 123778 |
| 18–64 | 353459 |
| 65+ | 134207 |
| Median household income | 70492 |
| Poverty rate | 11.1 |
| Homeownership rate | 75.72 |
| Unemployment rate | 4.9 |
| Median home value | 300900 |
| Gini index | 0.4591 |
| Vacancy rate | 13.13 |
| White | 439280 |
| Black | 38840 |
| Asian | 20903 |
| Native | 2088 |
| Hispanic/Latino | 113819 |
| Bachelor's or higher | 176649 |

## Districts

- [FL-12](/us/states/fl/districts/12.md) — 61% (congressional)
- [FL-15](/us/states/fl/districts/15.md) — 15% (congressional)
- [FL Senate District 23](/us/states/fl/districts/senate/23.md) — 54% (state senate)
- [FL Senate District 21](/us/states/fl/districts/senate/21.md) — 14% (state senate)
- [FL Senate District 11](/us/states/fl/districts/senate/11.md) — 7% (state senate)
- [FL House District 54](/us/states/fl/districts/house/54.md) — 33% (state house)
- [FL House District 55](/us/states/fl/districts/house/55.md) — 30% (state house)
- [FL House District 56](/us/states/fl/districts/house/56.md) — 6% (state house)
- [FL House District 53](/us/states/fl/districts/house/53.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
