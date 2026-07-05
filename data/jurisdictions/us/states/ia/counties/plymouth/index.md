---
type: Jurisdiction
title: "Plymouth County, IA"
classification: county
fips: "19149"
state: "IA"
demographics:
  population: 25747
  population_under_18: 6443
  population_18_64: 14208
  population_65_plus: 5096
  median_household_income: 83251
  poverty_rate: 6.9
  homeownership_rate: 73.61
  unemployment_rate: 2.2
  median_home_value: 228900
  gini_index: 0.4074
  vacancy_rate: 5.31
  race_white: 23022
  race_black: 615
  race_asian: 135
  race_native: 110
  hispanic: 1653
  bachelors_plus: 4673
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/ia/districts/senate/7"
    rel: in-district
    area_weight: 0.5222
  - to: "us/states/ia/districts/senate/2"
    rel: in-district
    area_weight: 0.4771
  - to: "us/states/ia/districts/house/13"
    rel: in-district
    area_weight: 0.5222
  - to: "us/states/ia/districts/house/3"
    rel: in-district
    area_weight: 0.4771
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Plymouth County, IA

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25747 |
| Under 18 | 6443 |
| 18–64 | 14208 |
| 65+ | 5096 |
| Median household income | 83251 |
| Poverty rate | 6.9 |
| Homeownership rate | 73.61 |
| Unemployment rate | 2.2 |
| Median home value | 228900 |
| Gini index | 0.4074 |
| Vacancy rate | 5.31 |
| White | 23022 |
| Black | 615 |
| Asian | 135 |
| Native | 110 |
| Hispanic/Latino | 1653 |
| Bachelor's or higher | 4673 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 7](/us/states/ia/districts/senate/7.md) — 52% (state senate)
- [IA Senate District 2](/us/states/ia/districts/senate/2.md) — 48% (state senate)
- [IA House District 13](/us/states/ia/districts/house/13.md) — 52% (state house)
- [IA House District 3](/us/states/ia/districts/house/3.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
