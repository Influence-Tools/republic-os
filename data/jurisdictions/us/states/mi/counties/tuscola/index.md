---
type: Jurisdiction
title: "Tuscola County, MI"
classification: county
fips: "26157"
state: "MI"
demographics:
  population: 52980
  population_under_18: 10639
  population_18_64: 30722
  population_65_plus: 11619
  median_household_income: 63811
  poverty_rate: 12.84
  homeownership_rate: 86.41
  unemployment_rate: 5.98
  median_home_value: 149500
  gini_index: 0.4061
  vacancy_rate: 10.47
  race_white: 49299
  race_black: 620
  race_asian: 190
  race_native: 139
  hispanic: 2001
  bachelors_plus: 8597
districts:
  - to: "us/states/mi/districts/09"
    rel: in-district
    area_weight: 0.8768
  - to: "us/states/mi/districts/08"
    rel: in-district
    area_weight: 0.0139
  - to: "us/states/mi/districts/senate/26"
    rel: in-district
    area_weight: 0.5003
  - to: "us/states/mi/districts/senate/25"
    rel: in-district
    area_weight: 0.3898
  - to: "us/states/mi/districts/house/97"
    rel: in-district
    area_weight: 0.5014
  - to: "us/states/mi/districts/house/98"
    rel: in-district
    area_weight: 0.3527
  - to: "us/states/mi/districts/house/67"
    rel: in-district
    area_weight: 0.0359
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Tuscola County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 52980 |
| Under 18 | 10639 |
| 18–64 | 30722 |
| 65+ | 11619 |
| Median household income | 63811 |
| Poverty rate | 12.84 |
| Homeownership rate | 86.41 |
| Unemployment rate | 5.98 |
| Median home value | 149500 |
| Gini index | 0.4061 |
| Vacancy rate | 10.47 |
| White | 49299 |
| Black | 620 |
| Asian | 190 |
| Native | 139 |
| Hispanic/Latino | 2001 |
| Bachelor's or higher | 8597 |

## Districts

- [MI-09](/us/states/mi/districts/09.md) — 88% (congressional)
- [MI-08](/us/states/mi/districts/08.md) — 1% (congressional)
- [MI Senate District 26](/us/states/mi/districts/senate/26.md) — 50% (state senate)
- [MI Senate District 25](/us/states/mi/districts/senate/25.md) — 39% (state senate)
- [MI House District 97](/us/states/mi/districts/house/97.md) — 50% (state house)
- [MI House District 98](/us/states/mi/districts/house/98.md) — 35% (state house)
- [MI House District 67](/us/states/mi/districts/house/67.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
