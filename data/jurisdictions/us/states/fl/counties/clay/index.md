---
type: Jurisdiction
title: "Clay County, FL"
classification: county
fips: "12019"
state: "FL"
demographics:
  population: 227584
  population_under_18: 57102
  population_18_64: 70810
  population_65_plus: 99672
  median_household_income: 87820
  poverty_rate: 9.22
  homeownership_rate: 75.89
  unemployment_rate: 3.78
  median_home_value: 312500
  gini_index: 0.4017
  vacancy_rate: 5.91
  race_white: 159072
  race_black: 26854
  race_asian: 7004
  race_native: 473
  hispanic: 26029
  bachelors_plus: 59861
districts:
  - to: "us/states/fl/districts/04"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/fl/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/fl/districts/house/20"
    rel: in-district
    area_weight: 0.6594
  - to: "us/states/fl/districts/house/11"
    rel: in-district
    area_weight: 0.3404
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Clay County, FL

County jurisdiction — 35 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 227584 |
| Under 18 | 57102 |
| 18–64 | 70810 |
| 65+ | 99672 |
| Median household income | 87820 |
| Poverty rate | 9.22 |
| Homeownership rate | 75.89 |
| Unemployment rate | 3.78 |
| Median home value | 312500 |
| Gini index | 0.4017 |
| Vacancy rate | 5.91 |
| White | 159072 |
| Black | 26854 |
| Asian | 7004 |
| Native | 473 |
| Hispanic/Latino | 26029 |
| Bachelor's or higher | 59861 |

## Districts

- [FL-04](/us/states/fl/districts/04.md) — 100% (congressional)
- [FL Senate District 6](/us/states/fl/districts/senate/6.md) — 100% (state senate)
- [FL House District 20](/us/states/fl/districts/house/20.md) — 66% (state house)
- [FL House District 11](/us/states/fl/districts/house/11.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
