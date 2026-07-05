---
type: Jurisdiction
title: "Logan County, CO"
classification: county
fips: "08075"
state: "CO"
demographics:
  population: 20892
  population_under_18: 3757
  population_18_64: 13143
  population_65_plus: 3992
  median_household_income: 51829
  poverty_rate: 15.77
  homeownership_rate: 66.31
  unemployment_rate: 5.44
  median_home_value: 245300
  gini_index: 0.4628
  vacancy_rate: 6.15
  race_white: 17088
  race_black: 758
  race_asian: 127
  race_native: 146
  hispanic: 3596
  bachelors_plus: 4141
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/63"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Logan County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20892 |
| Under 18 | 3757 |
| 18–64 | 13143 |
| 65+ | 3992 |
| Median household income | 51829 |
| Poverty rate | 15.77 |
| Homeownership rate | 66.31 |
| Unemployment rate | 5.44 |
| Median home value | 245300 |
| Gini index | 0.4628 |
| Vacancy rate | 6.15 |
| White | 17088 |
| Black | 758 |
| Asian | 127 |
| Native | 146 |
| Hispanic/Latino | 3596 |
| Bachelor's or higher | 4141 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 1](/us/states/co/districts/senate/1.md) — 100% (state senate)
- [CO House District 63](/us/states/co/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
