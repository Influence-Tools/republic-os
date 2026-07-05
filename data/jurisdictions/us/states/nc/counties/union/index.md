---
type: Jurisdiction
title: "Union County, NC"
classification: county
fips: "37179"
state: "NC"
demographics:
  population: 250958
  population_under_18: 64232
  population_18_64: 152754
  population_65_plus: 33972
  median_household_income: 102900
  poverty_rate: 7.68
  homeownership_rate: 81.65
  unemployment_rate: 4.19
  median_home_value: 417300
  gini_index: 0.4452
  vacancy_rate: 5.19
  race_white: 173717
  race_black: 28009
  race_asian: 11323
  race_native: 1319
  hispanic: 33636
  bachelors_plus: 89028
districts:
  - to: "us/states/nc/districts/08"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/senate/35"
    rel: in-district
    area_weight: 0.717
  - to: "us/states/nc/districts/senate/29"
    rel: in-district
    area_weight: 0.2826
  - to: "us/states/nc/districts/house/55"
    rel: in-district
    area_weight: 0.5849
  - to: "us/states/nc/districts/house/69"
    rel: in-district
    area_weight: 0.221
  - to: "us/states/nc/districts/house/68"
    rel: in-district
    area_weight: 0.1937
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Union County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 250958 |
| Under 18 | 64232 |
| 18–64 | 152754 |
| 65+ | 33972 |
| Median household income | 102900 |
| Poverty rate | 7.68 |
| Homeownership rate | 81.65 |
| Unemployment rate | 4.19 |
| Median home value | 417300 |
| Gini index | 0.4452 |
| Vacancy rate | 5.19 |
| White | 173717 |
| Black | 28009 |
| Asian | 11323 |
| Native | 1319 |
| Hispanic/Latino | 33636 |
| Bachelor's or higher | 89028 |

## Districts

- [NC-08](/us/states/nc/districts/08.md) — 100% (congressional)
- [NC Senate District 35](/us/states/nc/districts/senate/35.md) — 72% (state senate)
- [NC Senate District 29](/us/states/nc/districts/senate/29.md) — 28% (state senate)
- [NC House District 55](/us/states/nc/districts/house/55.md) — 58% (state house)
- [NC House District 69](/us/states/nc/districts/house/69.md) — 22% (state house)
- [NC House District 68](/us/states/nc/districts/house/68.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
