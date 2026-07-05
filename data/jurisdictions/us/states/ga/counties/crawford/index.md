---
type: Jurisdiction
title: "Crawford County, GA"
classification: county
fips: "13079"
state: "GA"
demographics:
  population: 12225
  population_under_18: 2547
  population_18_64: 7208
  population_65_plus: 2470
  median_household_income: 67116
  poverty_rate: 11.6
  homeownership_rate: 81.38
  unemployment_rate: 2.4
  median_home_value: 164100
  gini_index: 0.4436
  vacancy_rate: 15.35
  race_white: 8858
  race_black: 2572
  race_asian: 34
  race_native: 79
  hispanic: 481
  bachelors_plus: 1829
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/senate/18"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/134"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Crawford County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12225 |
| Under 18 | 2547 |
| 18–64 | 7208 |
| 65+ | 2470 |
| Median household income | 67116 |
| Poverty rate | 11.6 |
| Homeownership rate | 81.38 |
| Unemployment rate | 2.4 |
| Median home value | 164100 |
| Gini index | 0.4436 |
| Vacancy rate | 15.35 |
| White | 8858 |
| Black | 2572 |
| Asian | 34 |
| Native | 79 |
| Hispanic/Latino | 481 |
| Bachelor's or higher | 1829 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 18](/us/states/ga/districts/senate/18.md) — 100% (state senate)
- [GA House District 134](/us/states/ga/districts/house/134.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
