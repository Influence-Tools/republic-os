---
type: Jurisdiction
title: "Garland County, AR"
classification: county
fips: "05051"
state: "AR"
demographics:
  population: 100035
  population_under_18: 19821
  population_18_64: 55512
  population_65_plus: 24702
  median_household_income: 57181
  poverty_rate: 15.8
  homeownership_rate: 69.38
  unemployment_rate: 5.69
  median_home_value: 194300
  gini_index: 0.4603
  vacancy_rate: 17.23
  race_white: 82699
  race_black: 7606
  race_asian: 671
  race_native: 421
  hispanic: 7484
  bachelors_plus: 25200
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ar/districts/senate/6"
    rel: in-district
    area_weight: 0.8436
  - to: "us/states/ar/districts/senate/7"
    rel: in-district
    area_weight: 0.1562
  - to: "us/states/ar/districts/house/85"
    rel: in-district
    area_weight: 0.6605
  - to: "us/states/ar/districts/house/84"
    rel: in-district
    area_weight: 0.1829
  - to: "us/states/ar/districts/house/90"
    rel: in-district
    area_weight: 0.0749
  - to: "us/states/ar/districts/house/91"
    rel: in-district
    area_weight: 0.0471
  - to: "us/states/ar/districts/house/89"
    rel: in-district
    area_weight: 0.0344
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Garland County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 100035 |
| Under 18 | 19821 |
| 18–64 | 55512 |
| 65+ | 24702 |
| Median household income | 57181 |
| Poverty rate | 15.8 |
| Homeownership rate | 69.38 |
| Unemployment rate | 5.69 |
| Median home value | 194300 |
| Gini index | 0.4603 |
| Vacancy rate | 17.23 |
| White | 82699 |
| Black | 7606 |
| Asian | 671 |
| Native | 421 |
| Hispanic/Latino | 7484 |
| Bachelor's or higher | 25200 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 6](/us/states/ar/districts/senate/6.md) — 84% (state senate)
- [AR Senate District 7](/us/states/ar/districts/senate/7.md) — 16% (state senate)
- [AR House District 85](/us/states/ar/districts/house/85.md) — 66% (state house)
- [AR House District 84](/us/states/ar/districts/house/84.md) — 18% (state house)
- [AR House District 90](/us/states/ar/districts/house/90.md) — 7% (state house)
- [AR House District 91](/us/states/ar/districts/house/91.md) — 5% (state house)
- [AR House District 89](/us/states/ar/districts/house/89.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
