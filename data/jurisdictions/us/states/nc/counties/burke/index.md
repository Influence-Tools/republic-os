---
type: Jurisdiction
title: "Burke County, NC"
classification: county
fips: "37023"
state: "NC"
demographics:
  population: 87795
  population_under_18: 16168
  population_18_64: 52596
  population_65_plus: 19031
  median_household_income: 58592
  poverty_rate: 15.58
  homeownership_rate: 74.52
  unemployment_rate: 4.38
  median_home_value: 185400
  gini_index: 0.4426
  vacancy_rate: 10.04
  race_white: 70844
  race_black: 5405
  race_asian: 3108
  race_native: 619
  hispanic: 7457
  bachelors_plus: 18465
districts:
  - to: "us/states/nc/districts/14"
    rel: in-district
    area_weight: 0.9969
  - to: "us/states/nc/districts/senate/46"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/86"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Burke County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 87795 |
| Under 18 | 16168 |
| 18–64 | 52596 |
| 65+ | 19031 |
| Median household income | 58592 |
| Poverty rate | 15.58 |
| Homeownership rate | 74.52 |
| Unemployment rate | 4.38 |
| Median home value | 185400 |
| Gini index | 0.4426 |
| Vacancy rate | 10.04 |
| White | 70844 |
| Black | 5405 |
| Asian | 3108 |
| Native | 619 |
| Hispanic/Latino | 7457 |
| Bachelor's or higher | 18465 |

## Districts

- [NC-14](/us/states/nc/districts/14.md) — 100% (congressional)
- [NC Senate District 46](/us/states/nc/districts/senate/46.md) — 100% (state senate)
- [NC House District 86](/us/states/nc/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
