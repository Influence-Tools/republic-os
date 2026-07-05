---
type: Jurisdiction
title: "Jackson County, GA"
classification: county
fips: "13157"
state: "GA"
demographics:
  population: 84757
  population_under_18: 21285
  population_18_64: 51174
  population_65_plus: 12298
  median_household_income: 89544
  poverty_rate: 7.31
  homeownership_rate: 79.33
  unemployment_rate: 3.4
  median_home_value: 345000
  gini_index: 0.3922
  vacancy_rate: 7.62
  race_white: 66208
  race_black: 6457
  race_asian: 1997
  race_native: 481
  hispanic: 9201
  bachelors_plus: 21310
districts:
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.9952
  - to: "us/states/ga/districts/senate/47"
    rel: in-district
    area_weight: 0.6403
  - to: "us/states/ga/districts/senate/50"
    rel: in-district
    area_weight: 0.3596
  - to: "us/states/ga/districts/house/31"
    rel: in-district
    area_weight: 0.4781
  - to: "us/states/ga/districts/house/120"
    rel: in-district
    area_weight: 0.3152
  - to: "us/states/ga/districts/house/32"
    rel: in-district
    area_weight: 0.1904
  - to: "us/states/ga/districts/house/119"
    rel: in-district
    area_weight: 0.0162
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Jackson County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 84757 |
| Under 18 | 21285 |
| 18–64 | 51174 |
| 65+ | 12298 |
| Median household income | 89544 |
| Poverty rate | 7.31 |
| Homeownership rate | 79.33 |
| Unemployment rate | 3.4 |
| Median home value | 345000 |
| Gini index | 0.3922 |
| Vacancy rate | 7.62 |
| White | 66208 |
| Black | 6457 |
| Asian | 1997 |
| Native | 481 |
| Hispanic/Latino | 9201 |
| Bachelor's or higher | 21310 |

## Districts

- [GA-09](/us/states/ga/districts/09.md) — 100% (congressional)
- [GA Senate District 47](/us/states/ga/districts/senate/47.md) — 64% (state senate)
- [GA Senate District 50](/us/states/ga/districts/senate/50.md) — 36% (state senate)
- [GA House District 31](/us/states/ga/districts/house/31.md) — 48% (state house)
- [GA House District 120](/us/states/ga/districts/house/120.md) — 32% (state house)
- [GA House District 32](/us/states/ga/districts/house/32.md) — 19% (state house)
- [GA House District 119](/us/states/ga/districts/house/119.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
