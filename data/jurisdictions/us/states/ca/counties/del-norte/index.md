---
type: Jurisdiction
title: "Del Norte County, CA"
classification: county
fips: "06015"
state: "CA"
demographics:
  population: 27107
  population_under_18: 5657
  population_18_64: 15898
  population_65_plus: 5552
  median_household_income: 67058
  poverty_rate: 12.95
  homeownership_rate: 70.08
  unemployment_rate: 6.4
  median_home_value: 342000
  gini_index: 0.4323
  vacancy_rate: 15.21
  race_white: 17396
  race_black: 682
  race_asian: 931
  race_native: 1659
  hispanic: 5396
  bachelors_plus: 5818
districts:
  - to: "us/states/ca/districts/02"
    rel: in-district
    area_weight: 0.8231
  - to: "us/states/ca/districts/senate/2"
    rel: in-district
    area_weight: 0.8253
  - to: "us/states/ca/districts/house/2"
    rel: in-district
    area_weight: 0.8253
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Del Norte County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27107 |
| Under 18 | 5657 |
| 18–64 | 15898 |
| 65+ | 5552 |
| Median household income | 67058 |
| Poverty rate | 12.95 |
| Homeownership rate | 70.08 |
| Unemployment rate | 6.4 |
| Median home value | 342000 |
| Gini index | 0.4323 |
| Vacancy rate | 15.21 |
| White | 17396 |
| Black | 682 |
| Asian | 931 |
| Native | 1659 |
| Hispanic/Latino | 5396 |
| Bachelor's or higher | 5818 |

## Districts

- [CA-02](/us/states/ca/districts/02.md) — 82% (congressional)
- [CA Senate District 2](/us/states/ca/districts/senate/2.md) — 83% (state senate)
- [CA House District 2](/us/states/ca/districts/house/2.md) — 83% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
